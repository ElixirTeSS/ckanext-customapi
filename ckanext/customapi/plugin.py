import json as json
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

# Required so that GET requests work
@toolkit.side_effect_free
def get_news(context,data_dict=None):
  # The actual custom API method
  #return {"hello":"world"}
  with open('/tmp/iann_events.json') as data_file:
    try:
      data = json.load(data_file)
    except Exception, e:
      data = {"exception":str(e)}
  return(data)

class CustomAPIPlugin(plugins.SingletonPlugin):
  plugins.implements(plugins.interfaces.IActions)

  def get_actions(self):
    # Registers the custom API method defined above
    return {'get_news': get_news}
