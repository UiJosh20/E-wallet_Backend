from rest_framework.views import APIView
from rest_framework.response import Response

class DataView(APIView):
    def get(self, request):
        data = {
            "name": "John Doe",
            "balance": 8899750,
           
            "recent_activities": [
                {"icon":"https://res.cloudinary.com/dubaep0qz/image/upload/v1736001034/ba8dpf4uwhltshodahwk.png","name": "Netflix Subscription", "amount": 15.99, "currency": "USD", "time":"5:25PM"},
                {'icon':'https://res.cloudinary.com/dubaep0qz/image/upload/v1736001181/jkuzp8vzkr7btuqfpaa6.png',"name": "Amazon Purchase", "amount": 10.50, "currency": "USD", "time":"8:25PM"},
                {'icon':'https://res.cloudinary.com/dubaep0qz/image/upload/v1736001181/cm7dtgxsdlatplke8ntn.png',"name": "Canva Subscription", "amount": 12.99, "currency": "USD", "time":"11:30AM"},
            ],
            "savings":[
                {
                    "icon":"https://res.cloudinary.com/dubaep0qz/image/upload/v1736005057/zj1x4j4fiapqnpdpse6z.png",
                    "name": "New Car",
                    "amount": 6000,
                },
                {
                    "icon":"https://res.cloudinary.com/dubaep0qz/image/upload/v1736005056/g9i2suxz5woak583ciy6.png",
                    "name": "New House",
                    "amount": 10000,
                },
                {
                    "icon":"https://res.cloudinary.com/dubaep0qz/image/upload/v1736005139/u6lkj1wrlt5hszehpmxu.png",
                    "name": "Vacation",
                    "amount": 5000,
                }
            ],
             "UID":" 8194638720",
        }
        return Response(data)
