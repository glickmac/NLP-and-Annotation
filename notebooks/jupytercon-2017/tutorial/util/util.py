
import io, os, sys, types
from IPython import get_ipython
from nbformat import read
from IPython.core.interactiveshell import InteractiveShell
from IPython.display import HTML
import urllib
from IPython.display import IFrame
html = """
<style>
#wrapper {{ width: 2000px; height: 1420px; padding: 0; overflow: hidden; }}
#scaled-frame {{ width: 2000px; height: 2000px; border: 0px; }}
#scaled-frame {{
    zoom: 0.71;
    -moz-transform: scale(0.71);
    -moz-transform-origin: 0 0;
    -o-transform: scale(0.71);
    -o-transform-origin: 0 0;
    -webkit-transform: scale(0.71);
    -webkit-transform-origin: 0 0;
}}

@media screen and (-webkit-min-device-pixel-ratio:0) {{
 #scaled-frame  {{ zoom: 1;  }}
}}
</style>
<!-- overflow: hidden;-->
<div id="wrapper" style="overflow: hidden; position: relative; left: -200px; width: {0}px ;height: {1}px">
    <iframe id="scaled-frame" src="{2}/"></iframe>
</div>
"""

def displacy(text, width=1500, height=300):
    body = {"model":'en', 'cpu':1, 'cph':1}
    query_string = urllib.parse.urlencode(body)
    url = "https://demos.explosion.ai/displacy/?{0}&text={1}"
    url = url.format(query_string, text.replace(" ", "%20"), )
    code = html.format(width, height, url)

    return HTML(code)



def has_subject_and_attribute(verb):
    children_depencies =list(map(lambda i: i.dep_, verb.children))
    return 'nsubj' in children_depencies and any(i in children_depencies for i in ('attr','acomp','dobj'))

def is_verb(token):
    return token.pos_ == 'VERB'

def extract_simple_relations(sentence):
    relations = []
    for VERB in filter(is_verb,sentence):
        if has_subject_and_attribute(VERB):
            for child in VERB.children:
                if child.dep_ == 'nsubj':
                    SUBJECT = child
                if child.dep_ in ('attr','acomp','dobj','pobj','prep'):
                    PROPERTY = list(child.subtree) 
            relation = {'subject':SUBJECT,'property':PROPERTY,'relation':VERB}
            relations.append(relation)
    return relations

