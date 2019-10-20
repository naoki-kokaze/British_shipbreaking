import re

def generate_DEPCHA_TEI_from_TSV(input_file, output_file):

    file = open(input_file, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()

    output_f = open(output_file, 'w', encoding='utf-8')
    n = '\n'

    ### Header Starts ###

    # Describe a bibliographical information of the source in the TEI/XML header
    # This include geographical information as well
    
    output_f.write("""<?xml version="1.0" encoding="UTF-8"?>
<?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>
<?xml-model href="http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng" type="application/xml"
	schematypens="http://purl.oclc.org/dsdl/schematron"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0">
      <teiHeader>
            <fileDesc>
                  <titleStmt>
                        <title>Thos. W. Ward Disbursement Ledger</title>
                  </titleStmt>
                  <publicationStmt>
                        <publisher>Naoki Kokaze</publisher>
                        <idno type="PID">o:depcha.ward_ledger.1</idno>
                        <availability>
                              <p/>
                        </availability>
                        <date when="2019-10-16">16 October 2019</date>
                  </publicationStmt>
                  <sourceDesc>
                        <msDesc>
                              <msIdentifier>
                                    <settlement>Newcastle, UK</settlement>
                                    <repository>Marine Technology Special Collection</repository>
                                    <collection>Companies: Shipbreaking. Ledgers &amp; publicity
                                          materials including T. W. Ward, British Iron &amp; Steel
                                          Corp; Hughes Bolckow</collection>
                                    <idno>S.124.3</idno>
                              </msIdentifier>
                              <msContents>
                                    <msItem>
                                          <author>Thos. W. Ward</author>
                                          <title>Ledger No. 2</title>
                                          <note>
                                                <p>Accounts of <orgName ana="bk:from"
                                                  ref="ThosWardLtd">Thos W. Ward Ltd</orgName> from
                                                  <date ana="bk:when" when="1934-06-01">June
                                                  1934</date>. </p>
                                          </note>
                                    </msItem>
                              </msContents>
                        </msDesc>
                        <listPlace>
                              <place xml:id="barrow">
                                    <placeName>Barrow</placeName>
                                    <location>
                                          <geo decls="#WGS">54.108967 -3.218894</geo>
                                    </location>
                              </place>
                              <place xml:id="briton_ferry">
                                    <placeName>Briton Ferry</placeName>
                                    <location>
                                          <geo decls="#WGS">51.632119 -3.824315</geo>
                                    </location>
                              </place>
                              <place xml:id="grays">
                                    <placeName>Grays</placeName>
                                    <location>
                                          <geo decls="#WGS">51.478404 0.323015</geo>
                                    </location>
                              </place>
                              <place xml:id="hayle">
                                    <placeName>Hayle</placeName>
                                    <location>
                                          <geo decls="#WGS">50.185467 -5.42091</geo>
                                    </location>
                              </place>
                              <place xml:id="inverkeithing">
                                    <placeName>Inverkeithing</placeName>
                                    <location>
                                          <geo decls="#WGS">56.030043 -3.398795</geo>
                                    </location>
                              </place>
                              <place xml:id="jarrow">
                                    <placeName>Jarrow</placeName>
                                    <location>
                                          <geo decls="#WGS">54.980297 -1.482757</geo>
                                    </location>
                              </place>
                              <place xml:id="lelant">
                                    <placeName>Lelant</placeName>
                                    <location>
                                          <geo decls="#WGS">50.183852 -5.440401</geo>
                                    </location>
                              </place>
                              <place xml:id="milford_haven">
                                    <placeName>Milford Haven</placeName>
                                    <location>
                                          <geo decls="#WGS">51.714306 -5.042697</geo>
                                    </location>
                              </place>
                              <place xml:id="pembroke">
                                    <placeName>Pembroke</placeName>
                                    <location>
                                          <geo decls="#WGS">51.674043 -4.908637</geo>
                                    </location>
                              </place>
                              <place xml:id="preston">
                                    <placeName>Preston</placeName>
                                    <location>
                                          <geo decls="#WGS">53.763201 -2.70309</geo>
                                    </location>
                              </place>
                        </listPlace>
                  </sourceDesc>
            </fileDesc>
            <encodingDesc>
                  <classDecl>
                        <taxonomy ana="bk:Taxonomy">
                              <category xml:id="HMS">
                                    <catDesc>His/Her Majesty's Ships of the British Royal
                                          Navy</catDesc>
                              </category>
                              <category xml:id="CV">
                                    <catDesc>Civilian Vessels</catDesc>
                              </category>
                        </taxonomy>
                  </classDecl>
            </encodingDesc>
      </teiHeader>
      <text>
            <body>""")

    ### End of the header description ###


    noise = re.compile('&amp;| |,')
    pageNum_check = '0'

    for index, line in enumerate(lines):
        if index == 0:
            pass
        else:
            line = line.rstrip()
            cols = line.split('\t')
            pageNum = cols[0]
            head = cols[1]
            place = cols[2]
            # place_ref = '#' + place.lower().replace(' ', '_')
            
            date = cols[3]
            if '/' in date:
                date = date[:-3]
            firm_name = cols[4].replace('&', '&amp;')

            # create a ref name for each firm by manipulating the string
            firm_ref = re.sub(noise, '', firm_name)
            firm_ref = '#' + firm_ref
        
            service = cols[5].replace('&', '&amp;')
            service_split = service.split(' ')
            commodity = service_split[0]
            commodity = re.sub(noise, '', commodity)

            try:
                ref = cols[6]
            except IndexError:
                ref = ""
            try:
                pound = cols[7]
            except IndexError:
                pound = ""
            try:
                shilling = cols[8]
            except IndexError:
                shilling = ""
            try:
                pence = cols[9]
            except IndexError:
                pence = ""
        
            if pageNum != "":
                if index != 1:
                    output_f.write(f'</table></div></div>{n}')
                output_f.write(f'<div><fw type="pageNum">{pageNum}</fw>{n}')
                output_f.write(f'<div><table><head>{head}<placeName>{place}</placeName></head>{n}')
        
            output_f.write(f'<row ana="bk:entry"><cell><date ana="bk:when" when="{date}"/></cell>{n}')
            output_f.write(f'<cell><name ana="bk:to" ref="{firm_ref}">{firm_name}</name>{n}')
            output_f.write(f'<measure ana="bk:service bk:to" commodity="{commodity}">{service}</measure></cell>{n}')
            output_f.write(f'<cell><rs>{ref}</rs></cell>{n}')
            if pound != "":
                output_f.write(f'<cell><measure ana="bk:money bk:from" commodity="Currency" quantity="{pound}" unit="pound">{pound}</measure></cell>{n}')
            if shilling != "":
                output_f.write(f'<cell><measure ana="bk:money bk:from" commodity="Currency" quantity="{shilling}" unit="shilling">{shilling}</measure></cell>{n}')
            if pence != "":
                output_f.write(f'<cell><measure ana="bk:money bk:from" commodity="Currency" quantity="{pence}" unit="pence">{pence}</measure></cell>{n}')
            output_f.write('</row>')

    output_f.write('</table></div></div></body></text></TEI>')
    output_f.close()



generate_DEPCHA_TEI_from_TSV('Ward_ledger_HMS_all.tsv', 'Ward_ledger_HMS_all.xml')
