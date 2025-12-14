import sys
import os
import time
import random
import json
import math
import threading
from datetime import datetime

class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

class Assets:
    LOGO = [
        "████████╗███████╗██████╗ ███╗   ███╗ █████╗  ██████╗  ██████╗ ████████╗ ██████╗██╗  ██╗██╗",
        "╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██╔══██╗██╔════╝ ██╔═══██╗╚══██╔══╝██╔════╝██║  ██║██║",
        "   ██║   █████╗  ██████╔╝██╔████╔██║███████║██║  ███╗██║   ██║   ██║   ██║     ███████║██║",
        "   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██╔══██║██║   ██║██║   ██║   ██║   ██║     ██╔══██║██║",
        "   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║  ██║╚██████╔╝╚██████╔╝   ██║   ╚██████╗██║  ██║██║",
        "   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝╚═╝  ╚═╝╚═╝"
    ]

    SPRITES = {
        "egg": [
            "      .---.      ",
            "     /     \\     ",
            "    |   ?   |    ",
            "     \\     /     ",
            "      '---'      "
        ],
        "baby": [
            "                 ",
            "     ( o . o )   ",
            "      (  _  )    ",
            "       \"---\"     ",
            "                 "
        ],
        "child": [
            "      /  _  \\    ",
            "     |  o o  |   ",
            "     (   w   )   ",
            "      \\_____/    ",
            "                 "
        ],
        "teen": [
            "      __v__      ",
            "     / - - \\     ",
            "    (   L   )    ",
            "     \\  ^  /     ",
            "      || ||      "
        ],
        "adult": [
            "      / ___ \\    ",
            "     | (o_o) |   ",
            "    /|  |_|  |\\  ",
            "   / |_______| \\ ",
            "     d       b   "
        ],
        "elder": [
            "      _,,,,,_    ",
            "     /  o o  \\   ",
            "    (|   =   |)  ",
            "    / \\_____/ \\  ",
            "   /    /|\\    \\ "
        ],
        "dead": [
            "      _______    ",
            "     /       \\   ",
            "    |  R.I.P  |  ",
            "    |         |  ",
            "    |_________|  "
        ],
        "sick": [
            "      ( @ _ @ )  ",
            "       ( ~~~ )   ",
            "      /       \\  "
        ]
    }

    ICONS = {
        "health": "♥",
        "hunger": "🍖",
        "energy": "⚡",
        "happy": "☺",
        "hygiene": "🚿",
        "gold": "💰",
        "crypto": "₿",
        "str": "⚔️",
        "int": "🔮",
        "dex": "🦶",
        "xp": "⭐",
        "skull": "💀",
        "poop": "💩",
        "sunny": "☀",
        "rainy": "☂",
        "cloudy": "☁",
        "night": "☾"
    }

class Data:
    ITEMS = {
        "apple": {"name": "Apple", "cost": 10, "type": "food", "val": 15, "desc": "A fresh red apple."},
        "burger": {"name": "Burger", "cost": 30, "type": "food", "val": 45, "desc": "Greasy but filling."},
        "steak": {"name": "Steak", "cost": 80, "type": "food", "val": 90, "desc": "Premium meat."},
        "coffee": {"name": "Coffee", "cost": 15, "type": "energy", "val": 30, "desc": "Hot bean juice."},
        "redbull": {"name": "RedBull", "cost": 40, "type": "energy", "val": 70, "desc": "Gives you wings."},
        "soap": {"name": "Soap", "cost": 10, "type": "hygiene", "val": 40, "desc": "Basic cleaning bar."},
        "shampoo": {"name": "Shampoo", "cost": 25, "type": "hygiene", "val": 80, "desc": "For silky fur."},
        "ball": {"name": "Ball", "cost": 20, "type": "toy", "val": 15, "desc": "Bouncy fun."},
        "console": {"name": "GameBox", "cost": 200, "type": "toy", "val": 50, "desc": "Next-gen gaming."},
        "medicine": {"name": "Medicine", "cost": 100, "type": "cure", "val": 0, "desc": "Cures all sickness."},
        "sword": {"name": "Iron Sword", "cost": 500, "type": "equip", "stat": "str", "val": 5, "desc": "+5 Strength"},
        "wand": {"name": "Magic Wand", "cost": 500, "type": "equip", "stat": "int", "val": 5, "desc": "+5 Intelligence"},
        "boots": {"name": "Speed Boots", "cost": 500, "type": "equip", "stat": "dex", "val": 5, "desc": "+5 Dexterity"}
    }

    ENEMIES = [
        {"name": "Slime", "hp": 30, "atk": 5, "xp": 10, "gold": 5},
        {"name": "Rat", "hp": 40, "atk": 8, "xp": 15, "gold": 8},
        {"name": "Wolf", "hp": 70, "atk": 15, "xp": 30, "gold": 20},
        {"name": "Goblin", "hp": 100, "atk": 20, "xp": 50, "gold": 35},
        {"name": "Orc", "hp": 180, "atk": 30, "xp": 100, "gold": 70},
        {"name": "Dragon", "hp": 500, "atk": 60, "xp": 500, "gold": 1000}
    ]

    TRAITS = {
        "brave": {"desc": "Damage +10%", "effect": "atk_up"},
        "smart": {"desc": "XP Gain +10%", "effect": "xp_up"},
        "glutton": {"desc": "Hunger drains faster, Heal +10%", "effect": "eat_up"},
        "lazy": {"desc": "Energy drains slower, XP Gain -10%", "effect": "lazy"},
        "filthy": {"desc": "Hygiene drains faster", "effect": "dirty"}
    }

class Utils:
    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def sleep(sec):
        time.sleep(sec)

    @staticmethod
    def typing_print(text, speed=0.01, color=Colors.WHITE, newline=True):
        sys.stdout.write(color)
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        if newline:
            sys.stdout.write(Colors.RESET + "\n")
        else:
            sys.stdout.write(Colors.RESET)

    @staticmethod
    def box_print(lines, width=60, title=""):
        print(f"{Colors.CYAN}╔{'═' * (width - 2)}╗{Colors.RESET}")
        if title:
            padding = (width - 2 - len(title)) // 2
            print(f"{Colors.CYAN}║{Colors.RESET}{' ' * padding}{Colors.BOLD}{Colors.WHITE}{title}{Colors.RESET}{' ' * (width - 2 - padding - len(title))}{Colors.CYAN}║{Colors.RESET}")
            print(f"{Colors.CYAN}╠{'═' * (width - 2)}╣{Colors.RESET}")
        for line in lines:
            clean_line = line.replace(Colors.RED, "").replace(Colors.GREEN, "").replace(Colors.YELLOW, "").replace(Colors.BLUE, "").replace(Colors.RESET, "").replace(Colors.BOLD, "")
            padding = width - 4 - len(clean_line)
            print(f"{Colors.CYAN}║{Colors.RESET} {line}{' ' * padding} {Colors.CYAN}║{Colors.RESET}")
        print(f"{Colors.CYAN}╚{'═' * (width - 2)}╝{Colors.RESET}")

    @staticmethod
    def draw_bar(val, max_val, length=20, color=Colors.GREEN):
        ratio = max(0, min(1, val / max_val))
        filled = int(ratio * length)
        bar = "█" * filled + "░" * (length - filled)
        return f"{color}{bar}{Colors.RESET}"

class Termagotchi:
    def __init__(self):
        self.save_file = "termagotchi.json"
        self.state = {
            "name": "Unknown",
            "born_at": time.time(),
            "last_save": time.time(),
            "age": 0,
            "stage": "egg",
            "trait": "none",
            "stats": {
                "health": 100,
                "max_health": 100,
                "hunger": 100,
                "energy": 100,
                "hygiene": 100,
                "happy": 100
            },
            "rpg": {
                "lvl": 1,
                "xp": 0,
                "max_xp": 100,
                "str": 5,
                "int": 5,
                "dex": 5
            },
            "wallet": {
                "gold": 100,
                "crypto": 0.0
            },
            "inventory": {},
            "status": {
                "sick": False,
                "sleeping": False,
                "poop_count": 0
            },
            "market": {
                "btc_price": 1000
            }
        }
        self.alive = True

    def load(self):
        if not os.path.exists(self.save_file):
            return False
        try:
            with open(self.save_file, 'r') as f:
                loaded = json.load(f)
                self.state.update(loaded)
            self.calc_offline_progress()
            return True
        except Exception:
            return False

    def save(self):
        self.state["last_save"] = time.time()
        with open(self.save_file, 'w') as f:
            json.dump(self.state, f, indent=4)

    def calc_offline_progress(self):
        now = time.time()
        diff = now - self.state["last_save"]
        hours = diff / 3600
        
        if hours > 0.5:
            Utils.typing_print(f"\n{Colors.YELLOW}[!] SYNCHRONIZING TIMELINE... {hours:.2f} HOURS PASSED.{Colors.RESET}")
            drain = int(hours * 10)
            
            trait = self.state["trait"]
            hunger_mult = 1.5 if trait == "glutton" else 1.0
            energy_mult = 0.5 if trait == "lazy" else 1.0
            
            if self.state["status"]["sleeping"]:
                self.state["stats"]["energy"] = 100
                self.state["status"]["sleeping"] = False
                Utils.typing_print(f"{Colors.GREEN}Your pet woke up fully rested.{Colors.RESET}")
            else:
                self.state["stats"]["energy"] = max(0, self.state["stats"]["energy"] - int(drain * energy_mult))

            self.state["stats"]["hunger"] = max(0, self.state["stats"]["hunger"] - int(drain * hunger_mult))
            self.state["stats"]["hygiene"] = max(0, self.state["stats"]["hygiene"] - drain)
            self.state["stats"]["happy"] = max(0, self.state["stats"]["happy"] - drain)
            
            poop_chance = min(1.0, hours * 0.2)
            if random.random() < poop_chance and self.state["stats"]["hunger"] > 0:
                self.state["status"]["poop_count"] += int(hours * 0.5) + 1
            
            if self.state["stats"]["hunger"] <= 0 or self.state["stats"]["hygiene"] <= 0:
                self.state["stats"]["health"] -= int(drain * 2)

            if self.state["status"]["poop_count"] > 3:
                self.state["status"]["sick"] = True
                self.state["stats"]["health"] -= 20

            if self.state["stats"]["health"] <= 0:
                self.die()

            
            change = random.uniform(-0.1, 0.1) * hours
            self.state["market"]["btc_price"] *= (1 + change)

    def die(self):
        self.state["stage"] = "dead"
        self.alive = False
        self.save()

    def check_evolution(self):
        st = self.state["stage"]
        age = self.state["age"]
        new_stage = st
        
        if st == "egg": new_stage = "baby"
        elif st == "baby" and age >= 2: new_stage = "child"
        elif st == "child" and age >= 10: new_stage = "teen"
        elif st == "teen" and age >= 25: new_stage = "adult"
        elif st == "adult" and age >= 60: new_stage = "elder"
        
        if new_stage != st:
            self.state["stage"] = new_stage
            Utils.clear()
            print("\n" * 5)
            Utils.typing_print(f"{Colors.MAGENTA}{Colors.BOLD}*** EVOLUTION EVENT ***{Colors.RESET}", 0.1)
            time.sleep(1)
            Utils.typing_print(f"{self.state['name']} is evolving into a {new_stage.upper()}!", 0.05)
            time.sleep(2)

    def tick(self):
        self.state["age"] += 0.01
        self.check_evolution()
        
        
        market_drift = random.uniform(-0.02, 0.02)
        self.state["market"]["btc_price"] *= (1 + market_drift)
        
        
        trait = self.state["trait"]
        
        h_dec = 0.5 * (1.5 if trait == "glutton" else 1.0)
        e_dec = 0.3 * (0.5 if trait == "lazy" else 1.0)
        hy_dec = 0.3 * (1.5 if trait == "filthy" else 1.0)
        
        if not self.state["status"]["sleeping"]:
            self.state["stats"]["hunger"] = max(0, self.state["stats"]["hunger"] - h_dec)
            self.state["stats"]["energy"] = max(0, self.state["stats"]["energy"] - e_dec)
            self.state["stats"]["happy"] = max(0, self.state["stats"]["happy"] - 0.2)
            self.state["stats"]["hygiene"] = max(0, self.state["stats"]["hygiene"] - hy_dec)
        else:
            self.state["stats"]["energy"] = min(100, self.state["stats"]["energy"] + 2.0)
            self.state["stats"]["hunger"] = max(0, self.state["stats"]["hunger"] - 0.1)

        
        if self.state["stats"]["hunger"] < 10 or self.state["stats"]["hygiene"] < 10:
            self.state["stats"]["health"] -= 0.5
        
        if self.state["status"]["poop_count"] > 0:
             self.state["stats"]["hygiene"] -= 0.5
             if self.state["stats"]["hygiene"] < 30 and not self.state["status"]["sick"]:
                 if random.random() < 0.05:
                     self.state["status"]["sick"] = True

        if self.state["status"]["sick"]:
            self.state["stats"]["health"] -= 0.5

        if self.state["stats"]["health"] <= 0:
            self.die()


        if self.state["stats"]["hunger"] > 0 and not self.state["status"]["sleeping"]:
             if random.random() < 0.005:
                 self.state["status"]["poop_count"] += 1

        self.save()

class Game:
    def __init__(self):
        self.pet = Termagotchi()
        self.running = True

    def start(self):
        Utils.clear()
        for line in Assets.LOGO:
            print(f"{Colors.GREEN}{line}{Colors.RESET}")
        print("\n")
        
        if not self.pet.load():
            Utils.typing_print("No saved pet found. Initializing new lifeform...", 0.05)
            self.create_pet()
        else:
            Utils.typing_print(f"Welcome back, Operator. Loading {self.pet.state['name']}...", 0.05)
            time.sleep(1)

        if self.pet.state["stage"] == "dead":
            self.game_over_screen()
        else:
            self.main_loop()

    def create_pet(self):
        Utils.clear()
        print(f"{Colors.BOLD}GENETIC ENGINEERING LAB{Colors.RESET}\n")
        name = input(f"{Colors.CYAN}Enter subject name: {Colors.RESET}")
        if not name: name = "Subject-01"
        
        print("\nSelect Genetic Trait:")
        traits = list(Data.TRAITS.keys())
        for i, t in enumerate(traits):
            print(f"[{i+1}] {t.upper()}: {Data.TRAITS[t]['desc']}")
        
        try:
            choice = int(input(f"\n{Colors.YELLOW}Selection > {Colors.RESET}")) - 1
            trait = traits[choice]
        except:
            trait = "none"

        self.pet.state["name"] = name
        self.pet.state["trait"] = trait
        self.pet.save()
        Utils.typing_print(f"\nGestating egg... {name} is born with trait [{trait.upper()}].")
        time.sleep(2)

    def game_over_screen(self):
        Utils.clear()
        print(f"\n{Colors.RED}{Colors.BOLD}SUBJECT TERMINATED.{Colors.RESET}")
        for line in Assets.SPRITES["dead"]:
            print(f"{Colors.RED}{line}{Colors.RESET}")
        print(f"\n{Colors.WHITE}{self.pet.state['name']} lived for {int(self.pet.state['age'])} days.{Colors.RESET}")
        print(f"\n[1] Delete Data & Restart")
        print(f"[2] Exit")
        
        if input("> ") == "1":
            os.remove(self.pet.save_file)
            self.pet = Termagotchi()
            self.create_pet()
            self.main_loop()
        else:
            sys.exit()

    def draw_ui(self):
        Utils.clear()
        p = self.pet.state
        
        
        hour = datetime.now().hour
        weather = "night" if hour < 6 or hour > 18 else "sunny"
        sky = Assets.ICONS[weather]
        
        
        print(f"{Colors.BG_BLUE}{Colors.WHITE}{Colors.BOLD} {p['name']} (Lv.{p['rpg']['lvl']}) {Colors.RESET} {Colors.BG_BLACK} {sky} {weather.upper()} {Colors.RESET} {Colors.BG_YELLOW}{Colors.BLACK} {Assets.ICONS['gold']} {p['wallet']['gold']} {Colors.RESET} {Colors.BG_MAGENTA}{Colors.WHITE} {Assets.ICONS['crypto']} {p['wallet']['crypto']:.4f} {Colors.RESET}")
        
        
        print(f"{Colors.CYAN}╔{'═'*58}╗{Colors.RESET}")
        
        sprite = Assets.SPRITES.get(p["stage"], Assets.SPRITES["egg"])
        if p["status"]["sick"]: sprite = Assets.SPRITES["sick"]
        if p["status"]["sleeping"]: 
            sprite = ["      z z Z Z    ", "     ( - . - )   ", "      (_____)    "]

        
        scene_lines = []
        scene_lines.append("")
        
        
        status_line = ""
        if p["status"]["sick"]: status_line += f"{Colors.RED}[SICK]{Colors.RESET} "
        if p["status"]["sleeping"]: status_line += f"{Colors.BLUE}[SLEEP]{Colors.RESET} "
        if p["stats"]["hunger"] < 20: status_line += f"{Colors.YELLOW}[HUNGRY]{Colors.RESET} "
        if p["stats"]["hygiene"] < 30: status_line += f"{Colors.GREEN}[STINKY]{Colors.RESET} "
        scene_lines.append(status_line.center(68))


        for line in sprite:
            color = Colors.GREEN
            if p["status"]["sick"]: color = Colors.RED
            if p["status"]["sleeping"]: color = Colors.BLUE
            scene_lines.append(f"{color}{line}{Colors.RESET}".center(68))

        
        poops = f"{Assets.ICONS['poop']} " * p["status"]["poop_count"]
        scene_lines.append(f"{poops}".center(58))
        
        for sl in scene_lines:
            print(f"{Colors.CYAN}║{Colors.RESET}{sl.ljust(68)}{Colors.CYAN}║{Colors.RESET}")

        print(f"{Colors.CYAN}╚{'═'*58}╝{Colors.RESET}")

        
        print(f" {Colors.RED}{Assets.ICONS['health']} HP: {Utils.draw_bar(p['stats']['health'], p['stats']['max_health'], 10, Colors.RED)} {Colors.GREEN}{Assets.ICONS['hunger']} FD: {Utils.draw_bar(p['stats']['hunger'], 100, 10, Colors.GREEN)}")
        print(f" {Colors.YELLOW}{Assets.ICONS['energy']} EN: {Utils.draw_bar(p['stats']['energy'], 100, 10, Colors.YELLOW)} {Colors.BLUE}{Assets.ICONS['hygiene']} CL: {Utils.draw_bar(p['stats']['hygiene'], 100, 10, Colors.BLUE)}")
        print(f" {Colors.MAGENTA}{Assets.ICONS['happy']} HP: {Utils.draw_bar(p['stats']['happy'], 100, 10, Colors.MAGENTA)} {Colors.CYAN}{Assets.ICONS['xp']} XP: {Utils.draw_bar(p['rpg']['xp'], p['rpg']['max_xp'], 10, Colors.CYAN)}")

        
        print(f"\n{Colors.UNDERLINE}COMMAND CONSOLE:{Colors.RESET}")
        print(f"{Colors.WHITE}[1] {Assets.ICONS['hunger']} FEED    [2] {Assets.ICONS['happy']} PLAY    [3] {Assets.ICONS['hygiene']} CLEAN   [4] {Assets.ICONS['energy']} SLEEP")
        print(f"[5] {Assets.ICONS['gold']} SHOP    [6] {Assets.ICONS['str']} WORK    [7] {Assets.ICONS['crypto']} STOCK   [8] {Assets.ICONS['skull']} ADVENTURE")
        print(f"[9] {Assets.ICONS['dex']} INV     [0] SYSTEM{Colors.RESET}")

    def main_loop(self):
        while self.pet.alive:
            self.draw_ui()
            self.pet.tick()
            
            print(f"\n{Colors.DIM}Input > {Colors.RESET}", end="")
            
            if os.name == 'nt':
                import msvcrt
                if msvcrt.kbhit():
                    choice = msvcrt.getch().decode('utf-8').lower()
                    self.handle_input(choice)
            else:
                import select
                i, o, e = select.select([sys.stdin], [], [], 1) 
                if i:
                    choice = sys.stdin.readline().strip()
                    self.handle_input(choice)
                else:
                    time.sleep(0.1)

            if self.pet.state["stage"] == "dead":
                self.game_over_screen()

    def handle_input(self, choice):
        p = self.pet.state
        if p["status"]["sleeping"] and choice not in ['4', '0']:
            Utils.typing_print(f"{Colors.RED}Shhh! {p['name']} is sleeping! Wake them up first.{Colors.RESET}")
            time.sleep(1)
            return

        if choice == '1': self.menu_feed()
        elif choice == '2': self.menu_play()
        elif choice == '3': self.action_clean()
        elif choice == '4': self.action_sleep()
        elif choice == '5': self.menu_shop()
        elif choice == '6': self.menu_work()
        elif choice == '7': self.menu_stock()
        elif choice == '8': self.menu_adventure()
        elif choice == '9': self.menu_inventory()
        elif choice == '0':
            self.pet.save()
            sys.exit()

    def menu_feed(self):
        Utils.clear()
        print(f"{Colors.GREEN}=== KITCHEN ==={Colors.RESET}")
        inv = self.pet.state["inventory"]
        foods = [k for k in inv if Data.ITEMS[k]["type"] == "food"]
        
        if not foods:
            print("You have no food! Go to the Shop.")
            time.sleep(1)
            return

        for i, k in enumerate(foods):
            print(f"[{i+1}] {Data.ITEMS[k]['name']} (x{inv[k]})")
        print("[0] Cancel")

        try:
            sel = int(input("> ")) - 1
            if sel == -1: return
            item = foods[sel]
            self.use_item(item)
        except: pass

    def use_item(self, item_key):
        p = self.pet.state
        data = Data.ITEMS[item_key]
        
        p["inventory"][item_key] -= 1
        if p["inventory"][item_key] <= 0:
            del p["inventory"][item_key]

        Utils.typing_print(f"Using {data['name']}...", 0.05)
        
        if data["type"] == "food":
            p["stats"]["hunger"] = min(100, p["stats"]["hunger"] + data["val"])
            p["stats"]["health"] = min(p["stats"]["max_health"], p["stats"]["health"] + 2)
        elif data["type"] == "energy":
            p["stats"]["energy"] = min(100, p["stats"]["energy"] + data["val"])
        elif data["type"] == "hygiene":
            p["stats"]["hygiene"] = min(100, p["stats"]["hygiene"] + data["val"])
        elif data["type"] == "cure":
            p["status"]["sick"] = False
            p["stats"]["health"] = 100
            print(f"{Colors.GREEN}Cured!{Colors.RESET}")
        elif data["type"] == "equip":
            stat = data["stat"]
            p["rpg"][stat] += data["val"]
            print(f"{Colors.MAGENTA}Equipped! {stat.upper()} increased.{Colors.RESET}")
        
        time.sleep(1)

    def menu_play(self):
        Utils.clear()
        print(f"{Colors.YELLOW}=== GAMEROOM ==={Colors.RESET}")
        print("[1] Guess the Number (Cost: 5 En)")
        print("[2] Slot Machine (Cost: 10 Gold)")
        print("[3] Math Quiz (Cost: 10 En)")
        print("[0] Back")
        
        c = input("> ")
        if c == '1': self.game_guess()
        elif c == '2': self.game_slots()
        elif c == '3': self.game_math()

    def game_guess(self):
        p = self.pet.state
        if p["stats"]["energy"] < 5:
            print("Too tired.")
            return
        p["stats"]["energy"] -= 5
        
        secret = random.randint(1, 10)
        print("I'm thinking of a number 1-10.")
        try:
            g = int(input("Guess: "))
            if g == secret:
                print(f"{Colors.GREEN}Correct! +20 Happy, +10 Gold{Colors.RESET}")
                p["stats"]["happy"] = min(100, p["stats"]["happy"] + 20)
                p["wallet"]["gold"] += 10
            else:
                print(f"{Colors.RED}Wrong! It was {secret}.{Colors.RESET}")
        except: pass
        time.sleep(1)

    def game_slots(self):
        p = self.pet.state
        if p["wallet"]["gold"] < 10:
            print("Not enough gold.")
            return
        p["wallet"]["gold"] -= 10
        
        syms = ["🍒", "🍋", "🔔", "💎", "7️⃣"]
        r1 = random.choice(syms)
        r2 = random.choice(syms)
        r3 = random.choice(syms)
        
        print(f"\n{Colors.BG_WHITE}{Colors.BLACK} {r1} | {r2} | {r3} {Colors.RESET}\n")
        
        if r1 == r2 == r3:
            prize = 500 if r1 == "7️⃣" else 100
            print(f"{Colors.BOLD}{Colors.YELLOW}JACKPOT! Win {prize} Gold!{Colors.RESET}")
            p["wallet"]["gold"] += prize
            p["stats"]["happy"] = 100
        elif r1 == r2 or r2 == r3 or r1 == r3:
            print(f"{Colors.GREEN}Match! Win 20 Gold.{Colors.RESET}")
            p["wallet"]["gold"] += 20
        else:
            print("Loser.")
        time.sleep(2)

    def game_math(self):
        p = self.pet.state
        if p["stats"]["energy"] < 10:
            print("Too tired.")
            return
        p["stats"]["energy"] -= 10
        
        a = random.randint(10, 99)
        b = random.randint(10, 99)
        ans = a + b
        
        start = time.time()
        print(f"Quick! What is {a} + {b}?")
        try:
            u = int(input("> "))
            if u == ans and (time.time() - start) < 5:
                print(f"{Colors.CYAN}Genius! +2 INT, +10 XP{Colors.RESET}")
                p["rpg"]["int"] += 2
                self.gain_xp(10)
            else:
                print("Too slow or wrong.")
        except: pass
        time.sleep(1)

    def action_clean(self):
        p = self.pet.state
        if p["status"]["poop_count"] == 0:
            print("It's clean already.")
        else:
            print("Cleaning up...")
            time.sleep(1)
            p["status"]["poop_count"] = 0
            p["stats"]["hygiene"] = 100
            print(f"{Colors.GREEN}Sparkling!{Colors.RESET}")
        time.sleep(1)

    def action_sleep(self):
        p = self.pet.state
        p["status"]["sleeping"] = not p["status"]["sleeping"]
        print("Lights toggled.")
        time.sleep(0.5)

    def menu_shop(self):
        while True:
            Utils.clear()
            print(f"{Colors.YELLOW}=== GENERAL STORE ==={Colors.RESET}")
            print(f"Gold: {self.pet.state['wallet']['gold']}")
            items = list(Data.ITEMS.keys())
            for i, k in enumerate(items):
                d = Data.ITEMS[k]
                print(f"[{i+1}] {d['name'].ljust(12)} ${d['cost']} | {d['desc']}")
            print("[0] Exit")
            
            try:
                sel = int(input("Buy > ")) - 1
                if sel == -1: break
                key = items[sel]
                cost = Data.ITEMS[key]["cost"]
                if self.pet.state["wallet"]["gold"] >= cost:
                    self.pet.state["wallet"]["gold"] -= cost
                    self.pet.state["inventory"][key] = self.pet.state["inventory"].get(key, 0) + 1
                    print(f"{Colors.GREEN}Bought {key}!{Colors.RESET}")
                    time.sleep(0.5)
                else:
                    print(f"{Colors.RED}Too poor.{Colors.RESET}")
                    time.sleep(0.5)
            except: pass

    def menu_work(self):
        Utils.clear()
        p = self.pet.state
        if p["stats"]["energy"] < 30:
            print("Too tired to work.")
            time.sleep(1)
            return

        jobs = [
            {"name": "Janitor", "req": 0, "pay": 20, "stat": "str"},
            {"name": "Coder", "req": 10, "pay": 50, "stat": "int"},
            {"name": "Assassin", "req": 30, "pay": 150, "stat": "dex"}
        ]
        
        print("=== JOB BOARD ===")
        for i, j in enumerate(jobs):
            can_do = p["rpg"][j["stat"]] >= j["req"]
            color = Colors.GREEN if can_do else Colors.RED
            print(f"{color}[{i+1}] {j['name']} (Req: {j['req']} {j['stat'].upper()}) - Pay: ${j['pay']}{Colors.RESET}")
            
        try:
            sel = int(input("> ")) - 1
            job = jobs[sel]
            if p["rpg"][job["stat"]] >= job["req"]:
                print(f"Working as {job['name']}...")
                time.sleep(2)
                p["stats"]["energy"] -= 30
                p["stats"]["happy"] -= 10
                p["wallet"]["gold"] += job["pay"]
                print(f"{Colors.GREEN}Shift complete. Earned ${job['pay']}.{Colors.RESET}")
            else:
                print("Not qualified.")
        except: pass
        time.sleep(1)

    def menu_stock(self):
        while True:
            Utils.clear()
            p = self.pet.state
            price = p["market"]["btc_price"]
            print(f"{Colors.MAGENTA}=== CRYPTO EXCHANGE ==={Colors.RESET}")
            print(f"BTC Price: ${price:.2f}")
            print(f"Your Wallet: ${p['wallet']['gold']} | BTC: {p['wallet']['crypto']:.4f}")
            print("\n[1] Buy BTC")
            print("[2] Sell BTC")
            print("[0] Exit")
            
            c = input("> ")
            if c == '0': break
            
            try:
                amt = float(input("Amount ($ or BTC): "))
                if c == '1':
                    cost = amt
                    if p["wallet"]["gold"] >= cost:
                        btc = cost / price
                        p["wallet"]["gold"] -= cost
                        p["wallet"]["crypto"] += btc
                        print("Bought.")
                elif c == '2':
                    btc = amt
                    if p["wallet"]["crypto"] >= btc:
                        gold = btc * price
                        p["wallet"]["crypto"] -= btc
                        p["wallet"]["gold"] += gold
                        print("Sold.")
            except: pass

    def menu_inventory(self):
        Utils.clear()
        print(f"{Colors.CYAN}=== INVENTORY ==={Colors.RESET}")
        inv = self.pet.state["inventory"]
        if not inv: print("Empty.")
        else:
            for k, v in inv.items():
                print(f"{Data.ITEMS[k]['name']}: {v}")
        
        print(f"\nSTATS:")
        print(f"STR: {self.pet.state['rpg']['str']}")
        print(f"INT: {self.pet.state['rpg']['int']}")
        print(f"DEX: {self.pet.state['rpg']['dex']}")
        input("\n[Enter] to Back")

    def gain_xp(self, amount):
        p = self.pet.state
        if p["trait"] == "smart": amount = int(amount * 1.2)
        if p["trait"] == "lazy": amount = int(amount * 0.9)
        
        p["rpg"]["xp"] += amount
        print(f"{Colors.CYAN}+{amount} XP{Colors.RESET}")
        
        if p["rpg"]["xp"] >= p["rpg"]["max_xp"]:
            p["rpg"]["lvl"] += 1
            p["rpg"]["xp"] = 0
            p["rpg"]["max_xp"] = int(p["rpg"]["max_xp"] * 1.5)
            p["rpg"]["str"] += 2
            p["rpg"]["int"] += 2
            p["rpg"]["dex"] += 2
            p["stats"]["max_health"] += 20
            p["stats"]["health"] = p["stats"]["max_health"]
            print(f"{Colors.BOLD}{Colors.YELLOW}LEVEL UP! You are now Level {p['rpg']['lvl']}!{Colors.RESET}")
            time.sleep(2)

    def menu_adventure(self):
        p = self.pet.state
        if p["stats"]["energy"] < 20 or p["stats"]["health"] < 20:
            print("Too weak to fight.")
            time.sleep(1)
            return

        Utils.clear()
        print(f"{Colors.RED}=== DUNGEON ENTRANCE ==={Colors.RESET}")
        
        enemy_idx = min(len(Data.ENEMIES)-1, (p["rpg"]["lvl"] - 1) // 2)
        enemy_template = Data.ENEMIES[enemy_idx]
        
        enemy = enemy_template.copy()
        print(f"You encounter a {Colors.BOLD}{enemy['name']}{Colors.RESET}!")
        time.sleep(1)
        
        combat = True
        while combat:
            Utils.clear()
            print(f"{Colors.BOLD}COMBAT{Colors.RESET}")
            print(f"{p['name']} (HP: {p['stats']['health']}) vs {enemy['name']} (HP: {enemy['hp']})")
            print("----------------")
            print("[1] Attack")
            print("[2] Magic (Cost 10 En)")
            print("[3] Run")
            
            act = input("> ")
            
            dmg = 0
            if act == '1':
                crit = 2.0 if random.random() < (p["rpg"]["dex"]/100) else 1.0
                dmg = int((p["rpg"]["str"] * 1.5) * crit)
                if p["trait"] == "brave": dmg = int(dmg * 1.1)
                enemy["hp"] -= dmg
                print(f"You hit for {dmg}{' CRIT!' if crit>1 else ''}")
                
            elif act == '2':
                if p["stats"]["energy"] >= 10:
                    p["stats"]["energy"] -= 10
                    dmg = p["rpg"]["int"] * 3
                    enemy["hp"] -= dmg
                    print(f"You cast fireball for {dmg}!")
                else:
                    print("No energy!")
                    
            elif act == '3':
                if random.random() < 0.5:
                    print("Escaped!")
                    combat = False
                    break
                else:
                    print("Failed to run!")
            
            if enemy["hp"] <= 0:
                print(f"\n{Colors.GREEN}{Colors.BOLD}VICTORY!{Colors.RESET}")
                self.gain_xp(enemy["xp"])
                p["wallet"]["gold"] += enemy["gold"]
                print(f"Looted {enemy['gold']} Gold.")
                time.sleep(2)
                combat = False
                break
                
            edmg = max(1, enemy["atk"] - (p["rpg"]["dex"] // 2))
            p["stats"]["health"] -= edmg
            print(f"{enemy['name']} hits you for {edmg}.")
            
            if p["stats"]["health"] <= 0:
                print(f"{Colors.RED}You were defeated...{Colors.RESET}")
                p["stats"]["health"] = 1
                p["stats"]["energy"] = 0
                p["stats"]["happy"] = 0
                time.sleep(2)
                combat = False
                
            time.sleep(1)

if __name__ == "__main__":
    try:
        g = Game()
        g.start()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()
