from dataclasses import dataclass

import functions_framework


@dataclass
class GreetingRequest:
    first_name: str
    last_name: str

    # Required to deserialize the request
    @staticmethod
    def from_dict(req: dict) -> "GreetingRequest":
        return GreetingRequest(
            first_name=req["first_name"],
            last_name=req["last_name"],
        )


@dataclass
class GreetingResponse:
    message: str

    # Required to serialize the response
    def to_dict(self) -> dict:
        return {
            "message": self.message,
        }


@functions_framework.typed
def greeting(req: GreetingRequest):
    return GreetingResponse(message=f"Hello {req.first_name} {req.last_name}!")
