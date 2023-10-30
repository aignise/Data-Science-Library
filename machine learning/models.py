from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

def train_linear_model(features, target):
    """Train a linear regression model."""
    model = LinearRegression()
    model.fit(features, target)
    return model

def train_lasso_model(features, target, alpha=1.0):
    """Train a Lasso regression model."""
    model = Lasso(alpha=alpha)
    model.fit(features, target)
    return model

def train_ridge_model(features, target, alpha=1.0):
    """Train a Ridge regression model."""
    model = Ridge(alpha=alpha)
    model.fit(features, target)
    return model

def train_decision_tree(features, target, max_depth=None):
    """Train a decision tree model."""
    model = DecisionTreeRegressor(max_depth=max_depth)
    model.fit(features, target)
    return model

def train_random_forest(features, target, n_estimators=100):
    """Train a random forest model."""
    model = RandomForestRegressor(n_estimators=n_estimators)
    model.fit(features, target)
    return model
