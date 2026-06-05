def allocate_green_time(density):

    if density == "HIGH":
        return 30

    elif density == "MEDIUM":
        return 20

    else:
        return 10


def detect_vehicle(lane_item):
    """Helper used by the benchmark: accepts a (lane, count) tuple and
    returns a tuple (lane, dict) matching the pipeline's output format."""
    lane_name, count = lane_item

    if count < 5:
        density = "LOW"
    elif count < 15:
        density = "MEDIUM"
    else:
        density = "HIGH"

    return (
        lane_name,
        {
            "vehicles": count,
            "density": density,
            "green_time": allocate_green_time(density),
        },
    )


def controller_node(queue_in, queue_out):

    print("[NODE C] Started")

    analysis_data = queue_in.get()

    final_data = {}

    for lane, data in analysis_data.items():

        final_data[lane] = {
            "vehicles":
                data["vehicles"],

            "density":
                data["density"],

            "green_time":
                allocate_green_time(
                    data["density"]
                )
        }

    queue_out.put(final_data)

    print("[NODE C] Decision Complete")