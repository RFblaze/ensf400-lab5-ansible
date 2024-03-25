from ansible_runner import Runner, RunnerConfig
import ansible_runner
import yaml

file = open("hosts.yml", "r")
yaml_data = yaml.safe_load(file)

for host_name in yaml_data["app_group"]["hosts"]:
    print(f"Host Name: {host_name}")
    host_ip = yaml_data["app_group"]["hosts"][host_name]["ansible_host"]
    print(f"Host IP: {host_ip}")
    host_groups = []
    for group, hosts in yaml_data.items():
        if host_name in hosts.get('hosts', []):
            host_groups.append(group)

    print(f"Host Groups: {host_groups}")

for host_name in yaml_data["load_balancer"]["hosts"]:
    print(f"Host Name: {host_name}")
    host_ip = yaml_data["load_balancer"]["hosts"][host_name]["ansible_host"]
    print(f"Host IP: {host_ip}")
    host_groups = []
    for group, hosts in yaml_data.items():
        if host_name in hosts.get('hosts', []):
            host_groups.append(group)

    print(f"Host Groups: {host_groups}")

print()
print("Pinging...")
ansible_runner.run_command(
    executable_cmd="ansible",
    cmdline_args=["all:localhost", "-m", "ping"]
)