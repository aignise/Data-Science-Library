from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

def evaluate_model(model, test_features, test_target):
    """Evaluate a machine learning model's performance."""
    predictions = model.predict(test_features)
    mse = mean_squared_error(test_target, predictions)
    r2 = r2_score(test_target, predictions)
    mae = mean_absolute_error(test_target, predictions)
    return {'Mean Squared Error': mse, 'R^2 Score': r2, 'Mean Absolute Error': mae}

def cross_validate_model(model, features, target, cv=5):
    """Perform cross-validation on a machine learning model."""
    from sklearn.model_selection import cross_val_score
    mse_scores = cross_val_score(model, features, target, scoring='neg_mean_squared_error', cv=cv)
    r2_scores = cross_val_score(model, features, target, scoring='r2', cv=cv)
    return {'mse_scores': mse_scores, 'r2_scores': r2_scores}
