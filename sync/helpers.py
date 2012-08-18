from explorer.views import Directory

def create_hierarchy(path):
    path_tokens = path.split('/')
    
    traversed = ''
    for token in path_tokens:
        traversed = traversed + token
        try:
            new_dir = Directory.object.get(path=traversed)
        except:
            new_dir = Directory(path=traversed)
            new_dir.save()
        traversed = traversed + '/'
    return new_dir
