import paramiko

def establishCon():
    # Set the SSH parameters
    hostname = '192.168.50.10'
    port = 22  # Default SSH port is 22
    username = 'ubuntu'
    password = 'turtlebot'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname, port, username, password)
        return ssh  # Return the SSH client object
    except Exception as e:
        print(f"Failed to establish SSH connection: {str(e)}")
        return None

cmd = 'sudo python3 techtalk/pwm_indicator.py'

def doAction(ssh, command):
    if ssh:
        sudo_pass = 'turtlebot'
        stdin, stdout, stderr = ssh.exec_command(f'echo {sudo_pass} | {command}')
        print(stdout.read().decode())
    else:
        print("SSH connection not established. Cannot execute command.")



def headlights():

    command = 'sudo python3 scripts_final/led_head_lights.py'
    ssh_client = establishCon()
    doAction(ssh_client,command)
    
    doAction(ssh_client, '\x03')

    if ssh_client:
        ssh_client.close()

def onDelivery_led():
    print("test")
    commandled= 'sudo python3 scripts_final/led_on_delivery.py'
    ssh_client = establishCon()

    doAction(ssh_client,commandled)

    if ssh_client:
        ssh_client.close()

def onDelivery_lcd():
    print("test")
    commandled= 'sudo python3 py_scripts/lcd_test2.py'
    ssh_client = establishCon()
    doAction(ssh_client, '\x03')

    doAction(ssh_client,commandled)


    if ssh_client:
        ssh_client.close()

def readyForDelivery(): #funktioniert
    print('test')
    commandlcd = 'sudo python3 py_scripts/lcd_test.py'
    ssh_client = establishCon()
    doAction(ssh_client, '\x03')
    doAction(ssh_client,commandlcd)

    if ssh_client:
        ssh_client.close()

    
