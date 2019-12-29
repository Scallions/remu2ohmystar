
def convert(remufp,out,userid):
    import json
    from loguru import logger

    logger.info("Convert from {}", remufp)
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
        logger.debug("Convert repo {}", key)
        for tag in repos[key]:
            tag = get_tag(tag)
            logger.debug("Repo {} tag {}", key, tag)
            if tag in ohmystar_obj["data"].keys():
                ohmystar_obj["data"][tag].append(int(key))
            else:
                ohmystar_obj["data"][tag] = [int(key)]

    ohmystarout = open(out,"w")
    logger.info("Output to {}", out)
    json.dump(ohmystar_obj,ohmystarout)
    ohmystarout.close()
    logger.info("Covert end")