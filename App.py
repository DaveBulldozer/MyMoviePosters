import streamlit as st
import re
import requests
import os
from io import BytesIO
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from colorthief import ColorThief

# Set page config
st.set_page_config(
    page_title="Movie Poster Generator",
    page_icon="🎬",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #f093fb 0%, #f5576c 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .stSelectbox > div > div {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #f5576c;
        color: white;
        border: none;
    }
    .stButton>button:hover {
        background: #f093fb;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🎬 Movie Poster Generator</h1>
    <p>Create beautiful posters from movies using TMDB</p>
</div>
""", unsafe_allow_html=True)

# Sidebar for options
st.sidebar.header("⚙️ Settings")

# TMDB API Key input
tmdb_api_key = st.sidebar.text_input(
    "TMDB API Key",
    type="password",
    help="Get your free API key from https://www.themoviedb.org/settings/api"
)

# Font upload
uploaded_font = st.sidebar.file_uploader(
    "Upload Custom Font (Optional)",
    type=['ttf', 'otf'],
    help="Upload a .ttf or .otf font file for custom typography. Falls back to a default font if not provided."
)

# Output options
output_option = st.sidebar.selectbox(
    "Output Style",
    ["light", "dark", "transparent_light", "transparent_dark"],
    help="Choose the poster style and background"
)

# Canvas aspect ratio
canvas_choice = st.sidebar.selectbox(
    "Canvas Aspect Ratio",
    ["default", "A-series", "iPhone"],
    help="Select the poster dimensions"
)

# A-series sub-option
a_series_size = None
if canvas_choice == "A-series":
    a_series_size = st.sidebar.selectbox(
        "A-Series Size",
        ["A0", "A1", "A2", "A3", "A4"],
        index=4  # Default to A4
    )

# Main content area
st.header("🎬 Search for a Movie")

# Search input
movie_search = st.text_input(
    "Enter movie title:",
    placeholder="e.g., Inception, The Matrix, Interstellar...",
    help="Type the name of the movie you want to create a poster for"
)

# Process button
if st.button("🎨 Generate Poster", type="primary", use_container_width=True):
    if not tmdb_api_key:
        st.error("Please enter your TMDB API key in the sidebar first!")
    elif not movie_search:
        st.error("Please enter a movie title!")
    else:
        # Define a temporary font file path to be used later
        temp_font_path = None
        try:
            with st.spinner("Creating your poster... This might take a moment."):

                # TODO: Implement TMDB API functions
                def search_movie(query, api_key):
                    """
                    Search for movies by title using TMDB API
                    Returns list of movie results
                    """
                    # PLACEHOLDER
                    st.info("🚧 Search movie function - TO BE IMPLEMENTED")
                    return []

                def get_movie_details(movie_id, api_key):
                    """
                    Get detailed movie information including:
                    - Title
                    - Director
                    - Cast
                    - Release date
                    - Runtime
                    - Production companies
                    - Plot synopsis
                    - Poster path
                    """
                    # PLACEHOLDER
                    st.info("🚧 Get movie details function - TO BE IMPLEMENTED")
                    return {}

                def download_poster(poster_path, api_key):
                    """
                    Download high-resolution poster from TMDB
                    Base URL: https://image.tmdb.org/t/p/original/
                    """
                    # PLACEHOLDER
                    st.info("🚧 Download poster function - TO BE IMPLEMENTED")
                    return Image.new('RGB', (600, 900), color='gray')

                def extract_palette(image, color_count=5):
                    """
                    Extract color palette from poster image
                    """
                    # PLACEHOLDER (keeping this as it works the same)
                    try:
                        temp_buffer = BytesIO()
                        image.save(temp_buffer, format='JPEG')
                        temp_buffer.seek(0)
                        ct = ColorThief(temp_buffer)
                        palette = ct.get_palette(color_count=color_count, quality=10)
                        return palette
                    except Exception:
                        return [(80, 80, 80), (120, 120, 120), (160, 160, 160), (200, 200, 200), (220, 220, 220)]

                def create_movie_poster_jpeg(movie_info, poster_img, palette_colors, base_font_path,
                                             dark_mode=False, W_base=800, H_base=1200):
                    """
                    Create high-resolution movie poster with:
                    - Movie poster image
                    - Color palette swatches
                    - Movie title
                    - Director name
                    - Cast list (top billed actors)
                    - Release date
                    - Runtime
                    - Production company
                    """
                    # PLACEHOLDER
                    st.info("🚧 Create movie poster function - TO BE IMPLEMENTED")
                    return Image.new('RGB', (W_base, H_base), color='lightblue')

                def create_movie_poster_transparent(movie_info, poster_img, palette_colors, base_font_path,
                                                    dark_mode=False, W_base=800, H_base=1200):
                    """
                    Create high-resolution transparent movie poster
                    """
                    # PLACEHOLDER
                    st.info("🚧 Create transparent movie poster function - TO BE IMPLEMENTED")
                    return Image.new('RGBA', (W_base, H_base), color=(0, 0, 0, 0))

                # Determine canvas dimensions
                W_base, H_base = 800, 1200  # Default

                if canvas_choice == "A-series" and a_series_size:
                    A_SERIES_MM = {
                        "A0": (841, 1189), "A1": (594, 841), "A2": (420, 594),
                        "A3": (297, 420), "A4": (210, 297)
                    }
                    w_mm, h_mm = A_SERIES_MM[a_series_size]
                    DPI = 300
                    W_base = int(round(w_mm * DPI / 25.4))
                    H_base = int(round(h_mm * DPI / 25.4))
                elif canvas_choice == "iPhone":
                    W_base = 800
                    H_base = int(round(800 * 19.5 / 9))

                # Handle uploaded font
                if uploaded_font:
                    temp_font_path = "temp_font.ttf"
                    with open(temp_font_path, "wb") as f:
                        f.write(uploaded_font.getbuffer())

                # Set dark mode flag
                dark_flag = output_option in ["dark", "transparent_dark"]

                # TODO: Implement the actual workflow
                st.info("🚧 PLACEHOLDER: Movie search and poster generation workflow to be implemented")
                st.write("**Planned workflow:**")
                st.write("1. Search for movie using TMDB API")
                st.write("2. Let user select from search results if multiple matches")
                st.write("3. Fetch movie details and high-res poster")
                st.write("4. Extract color palette from poster")
                st.write("5. Generate formatted poster with movie info")
                st.write("6. Provide download button")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.error("Please check your settings and try again.")

        finally:
            # Clean up the temporary font file if it was created
            if temp_font_path and os.path.exists(temp_font_path):
                os.remove(temp_font_path)

# Footer
st.markdown("---")
st.markdown("🎬 **Powered by The Movie Database (TMDB)** | This product uses the TMDB API but is not endorsed or certified by TMDB.")
