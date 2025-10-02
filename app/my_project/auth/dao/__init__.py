from .orders.hydrological_objects_dao import HydrologicalObjectsDAO
from .orders.hydrological_objects_has_rivers_dao import HydrologicalObjectsHasRiversDAO
from .orders.measurement_locations_dao import MeasurementLocationsDAO
from .orders.meteorological_conditions_dao import MeteorologicalConditionsDAO
from .orders.regions_dao import RegionsDAO
from .orders.river_types_dao import RiverTypesDAO
from .orders.rivers_dao import RiversDAO
from .orders.users_dao import UsersDAO
from .orders.users_has_water_level_alerts_dao import UsersHasWaterLevelAlertsDAO
from .orders.water_level_alerts_dao import WaterLevelAlertsDAO
from .orders.water_levels_dao import WaterLevelsDAO
from .orders.water_levels_has_meteorological_conditions_dao import WaterLevelsHasMeteorologicalConditionsDAO

hydrological_objects_dao = HydrologicalObjectsDAO()
hydrological_objects_has_rivers_dao = HydrologicalObjectsHasRiversDAO()
measurement_locations_dao = MeasurementLocationsDAO()
meteorological_conditions_dao = MeteorologicalConditionsDAO()
regions_dao = RegionsDAO()
river_types_dao = RiverTypesDAO()
rivers_dao = RiversDAO()
users_dao = UsersDAO()
user_has_water_level_alerts_dao = UsersHasWaterLevelAlertsDAO()
water_level_alerts_dao = WaterLevelAlertsDAO()
water_levels_dao = WaterLevelsDAO()
water_levels_has_meteorological_conditions_dao = WaterLevelsHasMeteorologicalConditionsDAO()
