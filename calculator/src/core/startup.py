"""
create by MR.ROBOT-AG at June(6/5/2020)
----this class base us application --> for initializer or settingUp application
"""


class StartUp:
    def __init__(self):
        super(StartUp, self)
    
    def start_app(self):

        from commons.Services.observer_services_handler.observer_services_handler import ObserverServicesHandler
        
        param, service_path, package, number1, number2 = ObserverServicesHandler().observer_handler()

        from commons.Services.setting_up_concentrate.setting_up_concentrate import SettingUpConcentrate

        SettingUpConcentrate(param, service_path, package, number1, number2 ).setting_up()