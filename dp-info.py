import fileinput

def safeSnip(ln, splitter, index):
    # Safely snip the CDP value from a line
    try:
        result = ln.split(splitter)[index].strip()
    except IndexError:
        result = "Unavailable"
    return result


for line in fileinput.input():
    if "Device-ID (0x01)" in line:
        deviceTLV = safeSnip(line, "'", 1)
    elif "Address (0x02)" in line:
        addressTLV = safeSnip(line, ",", 2)
    elif "Port-ID (0x03)" in line:
        portTLV = safeSnip(line, "'", 1)
    elif "Capability (0x04)" in line:
        capabilityTLV = safeSnip(line, ":", 3)
    elif "Software" in line:
        versionTLV = safeSnip(line, ",", 2)
    elif "Platform (0x06)" in line:
        platformTLV = safeSnip(line, "'", 1)
    elif "VTP Management Domain (0x09)" in line:
        vtpTLV = safeSnip(line,"'",1)
    elif "Duplex (0x0b)" in line:
        duplexTLV = safeSnip(line,":",2)

print("Device: %s" % deviceTLV)
print("Port: %s" % portTLV)
print("Platform: %s" % platformTLV)
print("Version: %s" % versionTLV)
print("Address: %s" % addressTLV)
print("Capabilities: %s" % capabilityTLV)
print("VTP Domain: %s" % vtpTLV)
print("Duplex: %s" % duplexTLV)

