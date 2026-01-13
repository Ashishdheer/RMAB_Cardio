🧠 Dynamic Treatment Plan Optimization for Chronic Disease Management using Restless Multi-Armed Bandits

This repository contains the implementation of a Restless Multi-Armed Bandit (RMAB) based framework for optimizing long-term treatment strategies in chronic disease management using real-world clinical data.

The project models each patient as a restless arm whose health state evolves over time, even when not actively treated, enabling the system to learn which patients should receive limited medical interventions at each time step to maximize overall health outcomes.

📌 The framework is evaluated on MIMIC-III ICU data, focusing on learning data-driven treatment policies under realistic clinical and budget constraints.



🔬 Key Features

🏥 Patient-as-Arm RMAB formulation

📊 Off-policy evaluation (WIS, ESS) for clinical safety

🤖 Learning optimal treatment policies from historical trajectories

⚖️ Handles limited treatment budgets & delayed health effects

🧪 Supports policy comparison, tuning, and ablation studies



🎯 Research Objective

To design a scalable, interpretable, and clinically meaningful RMAB framework that can assist in deciding which patients to treat, when, and how, while maximizing population-level health benefits under constrained medical resources.
