from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:

    app.register_blueprint(err_handler_bp)

    from .orders.hydrological_objects_route import hydrological_objects_bp
    from .orders.hydrological_objects_has_rivers_route import hydrological_objects_has_rivers_bp
    from .orders.measurement_locations_route import measurement_locations_bp
    from .orders.meteorological_conditions_route import meteorological_conditions_bp
    from .orders.regions_route import regions_bp
    from .orders.rivers_route import rivers_bp
    from .orders.river_types_route import river_types_bp
    from .orders.users_has_water_level_alerts_route import users_has_water_level_alerts_bp
    from .orders.users_route import users_bp
    from .orders.water_level_alerts_route import water_level_alerts_bp
    from .orders.water_levels_has_meteorological_conditions_route import water_levels_has_meteorological_conditions_bp
    from .orders.water_levels_route import water_levels_bp

    app.register_blueprint(hydrological_objects_bp)
    app.register_blueprint(hydrological_objects_has_rivers_bp)
    app.register_blueprint(measurement_locations_bp)
    app.register_blueprint(meteorological_conditions_bp)
    app.register_blueprint(regions_bp)
    app.register_blueprint(river_types_bp)
    app.register_blueprint(rivers_bp)
    app.register_blueprint(users_has_water_level_alerts_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(water_level_alerts_bp)
    app.register_blueprint(water_levels_has_meteorological_conditions_bp)
    app.register_blueprint(water_levels_bp)
