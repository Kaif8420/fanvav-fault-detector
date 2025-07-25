from sklearn.ensemble import RandomForestClassifier

class FaultDetector:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=50, max_depth=10, random_state=42)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def feature_importances(self, feature_names):
        import matplotlib.pyplot as plt
        importances = self.model.feature_importances_
        sorted_idx = importances.argsort()[::-1][:10]  # Top 10
        plt.figure(figsize=(10, 6))
        plt.barh([feature_names[i] for i in sorted_idx], importances[sorted_idx])
        plt.gca().invert_yaxis()
        plt.title("Top Feature Importances")
        plt.show()
