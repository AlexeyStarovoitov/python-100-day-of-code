import copy

class Item:
    def __init__(self,name, value):
        self.name = name
        self.value = value

class Box:
    def add(self, item):
        raise NotImplementedError()
    
    def count(self):
        raise NotImplementedError()
    
    def empty(self):
        raise NotImplementedError()
        
class ListBox(Box):
    def __init__(self):
        self.items = []
        super(ListBox, self).__init__()
    
    def add(self, item):
        self.items.append(item)
    
    def count(self):
        return len(self.items)
        
    def empty(self):
        items = copy.deepcopy(self.items)
        self.items.clear()
        return items

class DictBox(Box):
    def __init__(self):
        self.items = {}
        super(DictBox, self).__init__()
    
    def add(self, item):
        self.items[item.name] = item
    
    def count(self):
        return len(self.items)
        
    def empty(self):
        items = list(self.items.values())
        self.items.clear()
        return items      

def distribute(*args):
    
    all_items = []
    
    for box in args:
        all_items.append(box.empty())
        
    av_items_num = (int)(len(all_items)/len(args))
    
    for box in args:
        for i in range(av_items_num):
            box.add(all_items.pop())
            
    last_len = len(all_items)  
    for i in range(last_len):
        args(-1).add(all_items.pop())
        
        
if __name__ == '__main__':
    
    list_box1 = ListBox()
    list_box2 = ListBox()
    dict_box = DictBox()
    
    for i in range(20):
        item = Item(str(i), i)
        list_box1.add(item)
        
    for i in range(21, 29):
        item = Item(str(i), i)
        list_box2.add(item)
    
    for i in range(36, 41):
        item = Item(str(i), i)
        dict_box.add(item)
    
    print('Before')
    print(f'list_box1: {list_box1}\nlist_box2: {list_box2}\ndict_box: {dict_box}\n')
    distribute(list_box1, list_box2, dict_box)
    print('After')
    print(f'\nlist_box1: {list_box1}\nlist_box2: {list_box2}\ndict_box: {dict_box}\n')
    
    
    
    
    
    
    
    
    
        