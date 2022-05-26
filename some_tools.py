
feet_in_mile = 5280

def createfile(name):
    fx = open(name,"w")
    fx.close()
def modify_File(name,text):
    fm = open(name,"a")
    fm.write(text)
    fm.close()
def read_file(name):
    fmx = open(name,"r")
    return fmx.readlines()
def write_to_file(name,text):
    fn = open(name,"w")
    fn.write(text)
    fn.close()