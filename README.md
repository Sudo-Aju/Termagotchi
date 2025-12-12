<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Termagotchi Ultimate - Readme</title>
</head>
<body>
<h1>🥚 Termagotchi Ultimate</h1>
<p>
<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
<img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20MacOS-lightgrey?style=for-the-badge" alt="Platform">
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>
<p>
<strong>Termagotchi Ultimate</strong> is a feature-rich, persistent CLI (Command Line Interface) virtual pet simulation with RPG adventure elements, a dynamic economy, and a cryptocurrency stock market.
</p>
<p>
Your pet lives in your terminal, grows, evolves, and continues to age and consume resources even when the program is closed.
</p>
<hr>
<h2>🖥️ Preview</h2>
<pre>
 ╔══════════════════════════════════════════════════════════╗
 ║ [SLEEP]                  [SICK]                          ║
 ║                                                          ║
 ║                       ( @ _ @ )                          ║
 ║                        ( ~~~ )                           ║
 ║                       /       \                          ║
 ║                                                          ║
 ║                          💩                              ║
 ╚══════════════════════════════════════════════════════════╝
 ♥ HP: [████░░░░░░] 🍖 FD: [██░░░░░░░░]
 ⚡ EN: [████████░░] 🚿 CL: [░░░░░░░░░░]
</pre>
<h2>✨ Key Features</h2>
<ul>
<li><strong>🕰️ Persistence System:</strong> The game calculates time passed while offline. If you ignore your pet for 24 hours, you may return to a hungry, sick, or deceased pet.</li>
<li><strong>🧬 Evolution & Aging:</strong> Raise your pet from an <strong>Egg</strong> → <strong>Baby</strong> → <strong>Child</strong> → <strong>Teen</strong> → <strong>Adult</strong> → <strong>Elder</strong>.</li>
<li><strong>⚔️ RPG Adventure Mode:</strong> Equip weapons and armor, enter dungeons, fight enemies (from Slimes to Dragons), and gain XP to level up stats.</li>
<li><strong>📉 Dynamic Economy:</strong>
<ul>
<li><strong>Job Board:</strong> Work shifts based on your RPG stats (STR, INT, DEX).</li>
<li><strong>Crypto Market:</strong> Buy and sell Bitcoin (BTC) with a fluctuating real-time simulated price.</li>
<li><strong>Casino:</strong> Play slots or guessing games to win Gold.</li>
</ul>
</li>
<li><strong>🧠 Trait System:</strong> Choose a genetic trait at birth (e.g., <em>Glutton</em>, <em>Smart</em>, <em>Brave</em>) that affects gameplay stats.</li>
<li><strong>🎒 Inventory Management:</strong> Buy food, toys, hygiene products, and medicine from the shop.</li>
</ul>
<h2>🚀 Installation & Usage</h2>
<p><strong>No external dependencies required.</strong> This project uses standard Python libraries.</p>
<h3>1. Clone the repository</h3>
<pre><code>git clone https://github.com/yourusername/termagotchi.git
cd termagotchi</code></pre>
<h3>2. Run the application</h3>
<pre><code>python termagotchi.py</code></pre>
<h3>3. Controls</h3>
<p>Use the number keys <code>0-9</code> to navigate menus.</p>
<hr>
<h2>📖 Game Guide</h2>
<h3>1. Vitals & Needs</h3>
<p>Your pet has 5 main stats that decay over time:</p>
<ul>
<li><strong>Hunger (FD):</strong> Feed your pet via the Kitchen. Starvation causes health loss.</li>
<li><strong>Hygiene (CL):</strong> Poop accumulates over time. Clean it up or your pet will get sick.</li>
<li><strong>Energy (EN):</strong> Sleep restores energy. High energy is required for Working and Adventuring.</li>
<li><strong>Happiness (HP):</strong> Play games or buy toys to keep depression at bay.</li>
<li><strong>Health (HP):</strong> Drops if sick or starving. Reaches 0 = Death.</li>
</ul>
<h3>2. Genetic Traits</h3>
<p>When hatching a new egg, you can select a trait:</p>
<table>
<thead>
<tr>
<th>Trait</th>
<th>Effect</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>None</strong></td>
<td>Balanced stats.</td>
</tr>
<tr>
<td><strong>Brave</strong></td>
<td>Damage +10% in combat.</td>
</tr>
<tr>
<td><strong>Smart</strong></td>
<td>XP Gain +10%.</td>
</tr>
<tr>
<td><strong>Glutton</strong></td>
<td>Hunger drains faster, but Food heals +10% more HP.</td>
</tr>
<tr>
<td><strong>Lazy</strong></td>
<td>Energy drains slower, but XP gain is reduced.</td>
</tr>
<tr>
<td><strong>Filthy</strong></td>
<td>Hygiene drops rapidly.</td>
</tr>
</tbody>
</table>
<h3>3. Making Money</h3>
<ul>
<li><strong>Work:</strong> Go to the Job Board.
<ul>
<li><em>Janitor:</em> Requires basic Strength.</li>
<li><em>Coder:</em> Requires Intelligence.
<li><em>Assassin:</em> Requires Dexterity (High Pay).</li>
</ul>
</li>
<li><strong>Stock Market:</strong> Buy low, sell high. The BTC price fluctuates every tick and while offline.</li>
<li><strong>Gambling:</strong> Visit the Gameroom to play Slots.</li>
</ul>
<h3>4. Combat & Dungeons</h3>
<p>Select <strong>Adventure [8]</strong> to fight. Combat is turn-based.</p>
<ul>
<li><strong>Attack:</strong> Based on STR. Chance to Crit based on DEX.</li>
<li><strong>Magic:</strong> Costs Energy. Deals high damage based on INT.</li>
<li><strong>Loot:</strong> Winning grants Gold and XP.</li>
</ul>
<hr>
<h2>📂 File Structure</h2>
<ul>
<li><code>termagotchi.py</code>: The main source code.</li>
<li><code>termagotchi.json</code>: Created automatically on first run. Stores your save data.</li>
</ul>
<h2>🛠️ Technical Details</h2>
<ul>
<li><strong>Language:</strong> Python 3</li>
<li><strong>Libraries:</strong> <code>os</code>, <code>sys</code>, <code>time</code>, <code>json</code>, <code>random</code>, <code>math</code>, <code>threading</code></li>
<li><strong>Input Handling:</strong> Uses <code>msvcrt</code> for Windows and <code>select/tty</code> for Unix/Linux for responsive keyboard input without pressing Enter (where supported).</li>
</ul>
<h2>🤝 Contributing</h2>
<p>Pull requests are welcome!</p>
<ol>
<li>Fork the Project</li>
<li>Create your Feature Branch (<code>git checkout -b feature/AmazingFeature</code>)</li>
<li>Commit your Changes (<code>git commit -m 'Add some AmazingFeature'</code>)</li>
<li>Push to the Branch (<code>git push origin feature/AmazingFeature</code>)</li>
<li>Open a Pull Request</li>
</ol>
<h2>📝 License</h2>
<p>Distributed under the MIT License. See <code>LICENSE</code> for more information.</p>
<hr>
<p>
<strong>⚠️ Note:</strong> This is a simulation. If your pet dies, you must delete the save file (or select "Restart" in the game over screen) to try again. Take care of them!
</p>
</body>
</html># Termagotchi
