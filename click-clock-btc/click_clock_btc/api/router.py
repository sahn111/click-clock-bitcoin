from interfaces.generic_router import GenericRouter
from .service import BtcService

class BtcRouter(GenericRouter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.btc_service = BtcService()
        self.bind_routes()

    def bind_routes(self):
        self.get_router().get("/")(self.get_realtime_btc)

    def get_realtime_btc(self):

        btc = self.btc_service.get_realtime_btc()
        return btc    

    def pin_operation(self, email : str, phone : str, pin : str):
        pass
        # control email

        # control phone
        
        # control pin    

        # save pin