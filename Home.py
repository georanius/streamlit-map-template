import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Change the code of the side here: <https://github.com/georanius/streamlit-map-template?tab=readme-ov-file>, and ask for a merge request.
Or fork it, and create your own web-app.
Or you start like, I did with forking (https://github.com/opengeos/streamlit-map-template).
"""

st.sidebar.title("Doing coding in Geosciences")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/lWpD7ka.png"
st.sidebar.image(logo)

# Customize page title
st.title("Open)upyter Webpage")

st.markdown(
    """
    Ingredients:
    The python parcels,
    [streamlit](https://streamlit.io) and [leafmap](https://leafmap.org).
    used by the template
    It is an open-source project and you are very welcome to contribute to the [GitHub repository](https://github.com/opengeos/streamlit-map-template).
    """
)



m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)

st.header("Was made from:")

#markdown = """
#1. For the [GitHub repository](https://github.com/opengeos/streamlit-map-template) or [use it as a template](https://github.com/opengeos/streamlit-map-template/generate) for your own project.
#2. Customize the sidebar by changing the sidebar text and logo in each Python files.
#3. Find your favorite emoji from https://emojipedia.org.
#4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.

"""

st.markdown(markdown)
