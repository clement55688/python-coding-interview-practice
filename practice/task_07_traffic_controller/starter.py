class TrafficController:
    def __init__(self):
        self.color = "RED"
        self.emergency = False
        self.pedestrian_pending = False
        self.served_pedestrians = 0
        

    def handle(self, event: str) -> dict:
        if event not in {"timer", "pedestrian", "emergency", "clear"}:
            raise ValueError(f"Unknown event: {event}")
    
        if event == "emergency":
            self.color = "RED"
            self.emergency = True

        elif event == "clear":
            if not self.emergency:
                raise ValueError("Cannot clear when in not emergency mode.")

            self.emergency = False
            self.color = "RED"

        elif not self.emergency:
            if event == "pedestrian":
                self.pedestrian_pending = True

            elif self.color == "RED":
                self.color = "GREEN"
            
            elif self.color == "GREEN":
                self.color = "YELLOW"
                if self.pedestrian_pending:
                    self.pedestrian_pending = False
                    self.served_pedestrians += 1
            else: #YELLOW
                self.color = "RED"
        
        return self.snapshot()

    def snapshot(self) -> dict:
        return {
            "color": self.color,
            "emergency": self.emergency,
            "pedestrian_pending": self.pedestrian_pending,
            "served_pedestrians": self.served_pedestrians 
        }
