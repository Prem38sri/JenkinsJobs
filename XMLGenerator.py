import sys

def XMLGenerate(domain):

        dcxml = open('conf/deployconfig.xml','r')
        inp = open('input/machinebw.cfg','r')
        i = 0
        dcxmldata = dcxml.read()
        for bwmachine in inp:
                bwmachinename = bwmachine.rstrip()
                i = i + 1
                bind = open('conf/bindingbw.xml','r')
                binddata = bind.read()
                binddata = binddata.replace("BWMACHINE",bwmachinename)
                binddata = binddata.replace("PARNUMBER",str(i))
                dcxmldata = dcxmldata.replace('<!-- PARREPLACER -->',binddata)

        finalxml = "output/LogWriter_"+domain+".xml"
        outputfile = open(finalxml,'w')
        outputfile.write(dcxmldata)
        outputfile.close


        dcxml.close()
        bind.close()
        inp.close()
