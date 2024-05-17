def check_networks(log_list, network):
    """Check if the given network is present in the log list.

    Args:
        log_list: A list of strings representing the logs.
        network: The network to check for.

    Returns:
        True if the network is present in the log list, False otherwise.
    """

    for log in log_list:
        if network in log:
            return True

    return False

