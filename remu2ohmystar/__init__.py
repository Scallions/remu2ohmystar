
def convert(remufp,out,userid):
    import json
    remu = open(remufp)
    remu_obj = json.load(remu)
    remu.close()
    ohmystar_obj = {
        "user_id": userid,
        "name": "OhMyStar JSON Data",
        "data": {},
        "version": 1
    } 
    tags = remu_obj["tags"]
    repos = remu_obj["repoWithTags"]

    def get_tag(tag):
        for t in tags:
            if tag == t["id"]:
                return t["name"]
        return None

    for key in repos.keys():
        for tag in repos[key]:
            tag = get_tag(tag)
            if tag in ohmystar_obj["data"].keys():
                ohmystar_obj["data"][tag].append(int(key))
            else:
                ohmystar_obj["data"][tag] = [int(key)]

    ohmystarout = open(out,"w")
    json.dump(ohmystar_obj,ohmystarout)
    ohmystarout.close()