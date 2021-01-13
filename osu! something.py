import os
import sys
import shutil
import json
import re



if os.path.exists('beatmaps.json'):
    with open('beatmaps.json', 'r') as file:
        beatmapsDatabase = json.loads(file.read())
else:
    beatmapsDatabase = {'osu!':{}, 'new_maps':{}}



def scanSongs(loc, folder):
    if folder==0:
        return os.listdir(loc + r'\Songs')
    elif folder==1:
        return os.listdir(loc)

def getList(lis, folder, beatmaps=beatmapsDatabase):
    if folder==0:
        beatmaps['osu!'] = {}
        for i in range(len(lis)):
            k = re.search("([0-9])+", lis[i])
            if k:
                beatmaps['osu!'][k.group()] = lis[i]
    elif folder==1:
        beatmaps['new_maps'] = {}
        for i in range(len(lis)):
            k = re.search("([0-9])+", lis[i])
            if k:
                beatmaps['new_maps'][k.group()] = lis[i]

    return beatmaps
    
def updateList(beatmaps):
    with open('beatmaps.json', 'w') as file:
        file.write(json.dumps(beatmaps, indent=3))


def compareMaps(sets=beatmapsDatabase):
    found = []
    maps = []
    maps.append(list(sets['osu!']))
    maps.append(list(sets['new_maps']))
    
    for i in range(len(maps[1])):
        if maps[1][i] in maps[0]:
            found.append(maps[1][i])
    print(len(found))
    return found

def moveMaps(found, directory, sets=beatmapsDatabase):
    print("[ ! ] Please wait...\n")
    if os.path.exists(directory + '/duplicates') == False:
        os.mkdir(directory + '/duplicates')
    for i in range(len(found)):
        shutil.move(directory + '/' + sets['new_maps'][found[i]], directory + '/duplicates/' + sets['new_maps'][found[i]])
    return ("[ ! ] Done.\n")

def main():
   updateList(getList(scanSongs('F:/osu!', 0), 0))
   updateList(getList(scanSongs('F:/maps', 1), 1))
   moveMaps(compareMaps(), 'F:/maps')
    
main()
