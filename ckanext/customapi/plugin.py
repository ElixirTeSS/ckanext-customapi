import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

# Required so that GET requests work
@toolkit.side_effect_free
def get_news(context,data_dict=None):
  # The actual custom API method
  return {"hello":"world"}


class CustomAPIPlugin(plugins.SingletonPlugin):
  plugins.implements(plugins.interfaces.IActions)

  def get_actions(self):
    # Registers the custom API method defined above
    return {'get_news': get_news}

