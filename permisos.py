#!/usr/bin/env python3
from os import walk, chmod, chown
from os.path import join, islink
from pwd import getpwnam
from grp import getgrnam

pub_path = "/raid/igss02_md0/publico_001/Trabajos"
pri_name = "0-Admin"

own_uname = "aoleaga"
own_uid = getpwnam(own_uname).pw_uid

own_pugname = "ingesur"
own_pugid = getgrnam(own_pugname).gr_gid

own_prgname = "ingesuradm"
own_prgid = getgrnam(own_prgname).gr_gid

dirperm = 0o0770
filperm = 0o0660 

def permi(path, pu_uid, pu_gid, dirperm=0o0770, filperm=0o0660, pr_name=None, pr_uid=-1, pr_gid=-1, recursive=False):
    """
    Change owner of file at specified `path` to `galaxy`.
    """
    try:
        # chown(path, galaxy_uid, galaxy_gid)
        if recursive:
            for root, dirs, files in walk(path):
                for d in dirs:
                    dd = join(root,d)
                    if not islink(dd):
                        if pri_name in d: 
                            chown(dd, pr_uid, pr_gid)
                        else: 
                            chown(dd, pu_uid, pu_gid)
                        chmod(dd, dirperm)
                for f in files:                    
                    ff = join(root, f)
                    #print('f=',f,'\nff=',ff)
                    if not islink(ff):
                        if pri_name in ff:
                            chown(ff, pr_uid, pr_gid)
                        else:
                            chown(ff, pu_uid, pu_gid)
                        chmod(ff, filperm)
    except BaseException as e:
        print(str(e))

permi(pub_path,own_uid,own_pugid,dirperm,filperm,pri_name,own_uid,own_prgid,True)
