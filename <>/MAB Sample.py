import numpy as np

class RestlessMAB:
    def _init_(self, n_patients, n_treatments, restless_factor=0.1):
        self.n_patients = n_patients
        self.n_treatments = n_treatments
        self.restless_factor = restless_factor
        self.health_states = np.random.rand(n_patients)
        self.rewards = np.zeros((n_patients, n_treatments))
        self.action_counts = np.zeros((n_patients, n_treatments))

    def get_reward(self, patient, treatment):
        base_reward = (1 - self.health_states[patient]) * np.random.rand()
        treatment_effectiveness = np.random.rand() * 0.2 + 0.8
        return base_reward * treatment_effectiveness

    def update_health(self):
        self.health_states -= self.restless_factor * np.random.rand(self.n_patients)
        self.health_states = np.clip(self.health_states, 0, 1)

    def select_treatment(self, patient):
        epsilon = 0.1
        if np.random.rand() < epsilon:
            return np.random.randint(0, self.n_treatments)
        else:
            avg_rewards = self.rewards[patient] / (self.action_counts[patient] + 1e-5)
            return np.argmax(avg_rewards)

    def run(self, iterations=100):
        for t in range(iterations):
            for patient in range(self.n_patients):
                treatment = self.select_treatment(patient)
                reward = self.get_reward(patient, treatment)
                self.rewards[patient, treatment] += reward
                self.action_counts[patient, treatment] += 1
            self.update_health()
            if t % 10 == 0:
                print(f"Iteration {t}: Average Health State: {np.mean(self.health_states):.4f}")

if _name_ == "_main_":
    n_patients = 5
    n_treatments = 3
    rmab = RestlessMAB(n_patients, n_treatments)
    rmab.run(iterations=100)