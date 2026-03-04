

marked_2nd = {"ns": "green",
              "ew": "red"}

mission_16th = {"ns": "red",
                "ew": "green"}


def switch_lights(traffic_lights: dict[str, str]):
    for i,key in enumerate (traffic_lights.keys()):
        if traffic_lights[key] == "green" and "red" in traffic_lights.values():
            traffic_lights[key] = "yellow"
        elif traffic_lights[key] == "yellow" and "red" in traffic_lights.values():
            traffic_lights[key] = "red"
        elif sum(v == "red" for v in traffic_lights.values()) > 1 :
            traffic_lights[key] = "green"
            print("last case")
    assert "red" in traffic_lights.values(), "Eine Ampel muss Rot sein!" + str(traffic_lights)

switch_lights(marked_2nd)
switch_lights(mission_16th)