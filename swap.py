import os
def create_swap_file(file_path, size_mb):
    os.system(f"sudo dd if=/dev/zero of={file_path} bs=1M count={size_mb}")
    os.system(f"sudo chmod 600 {file_path}")
    os.system(f"sudo mkswap {file_path}")
def activate_swap(file_path):
    os.system(f"sudo swapon {file_path}")
def add_to_fstab(file_path):
    with open("/etc/fstab", "a") as fstab:
        fstab.write(f"{file_path} none swap sw 0 0\n")
def main():
    swap_file_path = "/swapfile" 
    swap_size_mb = 7168
    create_swap_file(swap_file_path, swap_size_mb)
    activate_swap(swap_file_path)
    add_to_fstab(swap_file_path)
    print("Swap setup completed.")
if __name__ == "__main__":
    main()