from ansible_runner import run

result = run(
    playbook="/workspaces/ensf400-lab5-ansible/hello.yml",
    inventory="hosts.yml",
    settings={
        'process_isolation_executable': '/home/codespace/.python/current/bin/python3'
    }
)

# Print the results
print("Playbook Status:", result.stats)

# Check for any errors
if result.status == 'successful':
    print("Playbook ran successfully!")
else:
    print("Playbook failed to execute. Check the logs for more details.")
    print("Failure Reason:", result.status)
    print("Runner Output:", result.stdout)
