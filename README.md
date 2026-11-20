# Group-9-Project-2-Math-300
Author contributions:

Isaac S. : All coding, minus some references pulled from previous activties. Setting up README.md and requirments.txt files.

Tia A. : First order equations, model definition, and parameters for the Lorenz equation. Model definition, and parameters for the Van der Pol oscillator

Logan G. : Deriving first order equations, model definition, and parameters for the Pendulum equation. Deriving Equations for the Van der Pol Oscillator function.

Prerequisites:
numpy
matplotlib
scipy

How to run:
1. Download or clone this repository
2. Open terminal or similar codespace in the directory containing this file
3. Run the program using python Solve_ivp_p2.py

Expectations:
The program should open up four matplot windows, three for the separate systems and one for the error of the pendulum system.

AI Disclosure:
Isaac S. :
Used Copilot built into VS code to autocomplete fixing minor bugs and syntax errors.

Logan G. :
None.

Tia A. : 
None

Explination of Graphs:
The error plot shows a linear relationship between the powers of rtol and accuracy of the solver for the pendulum system.

All other graphs show variations of initial conditions:
Pendulum: Different initial conditions change the size and shape of ocilating wave patterns but maintain the relationship between theta and omega.
Van der Pol: Different initial conditions change how long it takes to reach an ocilating behavior but the size and shape of waves stay similar.
Lorenz: Small variations in initial conditions greatly change the behavior of all variables, though X and Y stay nearly identical through all graphs. Some initial conditions begin the chaotic behavior faster then others.
