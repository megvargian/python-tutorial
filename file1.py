a = "Cisco Switch";
print(a.index("o"));
print(a.count("i"));
print("_".join(a));

print(a.find("C"));
print(a.find("z"));

print(a.lower());
print(a.upper());
print(a);

print(a.startswith("C"));
print(a.endswith("h"));
print(a.endswith("d"));

b = "    Cisco Switch     ";
print(b);
print(b.strip());
print(b.replace(" ", ""));

c = "$$$Cisco Switch$$$";
print(c);
print(c.strip("$"));

d = "Cisco,Juniper,HP,Avaya,Nortel";
print(d.split(","));

x = "Cisco";
y = "Switch";
print((x + y) * 3);
print("o" in x);
print("v" in x);
print("v" not in x);

print("Cisco model: %s, %d WAN slots, IOS %.1f" %("7200XR", 8, 15.4));
print("Cisco model: {1}, {0} WAN slots, IOS {2}".format("7200XR", 8, 15.4));

string1 = "O E2 10.110.8.9 [160/5] voa 10.119.254.6, 0:01:00, Ethernet2";
print(string1[5: 15]);
print(string1[:-5]);
print(string1[::2]);
print(string1[::-1]);