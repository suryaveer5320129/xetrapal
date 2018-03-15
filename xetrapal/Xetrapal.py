#coding: utf-8
import astra
import karma
import jeeva
import fbkarmas
import twkarmas
import colored


class Xetrapal(jeeva.Jeeva):
    def __init__(self,*args, **kwargs):
        super(Xetrapal,self).__init__(*args, **kwargs)
        self.vaahans={}
        self.astras={}
        self.update_astras()
        self.update_vaahans()
        self.save_profile()
    def update_astras(self):
        self.logger.info("Trying to update astras")
        astras={}
        if self.astras=={}:
            self.logger.warning("I dont seem to have any astras")
        else:
            for astraname in self.astras.keys():
                astras[astraname]=str(type(self.astras[astraname]))
    
        self.set_property("astras",astras)
        self.save_profile()
    
    def update_vaahans(self):
        self.logger.info("Trying to update vaahans")
        vaahans={}
        if self.vaahans=={}:
            self.logger.warning("I dont seem to have any vaahans")
        else:
            for vaahanname in self.vaahans.keys():
                vaahans[vaahanname]=str(type(self.vaahans[vaahanname]))
    
        self.set_property("vaahans",vaahans)
        self.save_profile()
    

    def add_vaahan(self,vaahan):
        self.vaahans[vaahan.name]=vaahan
        self.update_vaahans()
    
    def release_vaahan(self,vaahanname):
        self.logger.info("Releasing vaahan " + colored.stylize(vaahanname,colored.fg("violet")))
        vaahan=self.vaahans.pop(vaahanname)
        self.update_vaahans()
        return vaahan
        

    def add_astra(self,astraname,newastra):
        self.astras[astraname]=newastra
        self.update_astras()
        
    def drop_astra(self,astraname):
        self.logger.info("Dropping astra " + colored.stylize(astraname,colored.fg("violet")))
        droppedastra=self.astras.pop(astraname)
        self.update_astras()
        return droppedastra
    def start_karta(self):
        self.karta=jeeva.Karta.start(jeeva=self)

    def get_fb_astra(self,fbconfig=None):
        if fbconfig==None:
            if "Facebook" in self.config.sections():
                fbconfig=karma.get_section(self.config,"Facebook")
        if "fbbrowser" not in self.astras.keys():
           self.astras['fbbrowser']=astra.get_browser(logger=self.logger)
        self.karta.tell({"msg":"run","func":fbkarmas.fb_login,"args":(self.astras['fbbrowser'],astra.get_section(fbconfig,"Facebook")),"kwargs":{"logger":self.logger}})
    