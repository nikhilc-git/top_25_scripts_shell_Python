import sys, shutil, math

if len(sys.argv) < 3:
    print("please provide the mount path and threshold.")
    print("Usage: script.py <mounth path> <threshold>")
    sys.exit(1)

mount_path = sys.argv[1]
threshold = int(sys.argv[2])

print(f"path: {mount_path}")
print(f"Threshold: {threshold}")

total, used, free = shutil.disk_usage(mount_path)

#print(total_g, used_g, free_g)
per_used = int(math.ceil((used/total)*100))

if per_used > threshold:
    print(f"WARNING:: {mount_path} disk usage exceeds the threshold.\nActual Disk:{per_used}%\nThreshold:{threshold}%")
else:
    print(f"INFO:: {mount_path} disk usage is within the threshold value.\nActual Disk:{per_used}%\nThreshold:{threshold}%")
