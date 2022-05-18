import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

def app():
  # line 11 imports the image, while line 12 displays it onscreen
  image = Image.open('images\LogoDNA.jpg')
  st.image(image, use_column_width=True)

  st.header('Enter DNA sequence')
  sequence_input = ">DNA Query \nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"


  sequence = st.text_area("Sequence input", sequence_input, height=200)

  # text_area displays a multi-line text input widget
  sequence = sequence.splitlines()
  # line 32 removes the ">DNA Query \n" line, and only shows the nucleotide sequence
  sequence = sequence[1:]
  sequence= ''.join(sequence)
  sequence_segments= '\n'.join(sequence)

  st.write('''
  ***
  ''')
  ## Prints the input DNA sequence
  # st.header('INPUT (DNA Query)')
  # sequence

  st.header('Segmented DNA Sequence')
  st.markdown(sequence_segments)

  ## DNA nucleotide count
  st.header('DNA Nucleotide Count')

  # function binds nucleotide:count via a dictionary
  def DNA_nucleotide_count(seq):
    d = dict([
              ('A',seq.count('A')),
              ('C',seq.count('C')),
              ('G',seq.count('G')),
              ('T',seq.count('T'))
              ])
    return d

  # this uses the function to apply it to the sequence, and display it onscreen
  X = DNA_nucleotide_count(sequence)

   # Total Number of Nucleotide in Input DNA Sequence
  total_nucleotides = X['A'] + X['C'] + X['G'] + X['T']
  st.subheader('This DNA sequence has  ' + str(total_nucleotides) + ' nucleotides.')

  title_colors = {
    'A': f'<p style="font-family:sans-serif; color:#5463FF; font-size: 20px;">There are {str(X["A"])}' + ' adenine (A).</p>',
    'C': f'<p style="font-family:sans-serif; color:#FF6C00; font-size: 20px;">There are {str(X["C"])}' + ' cytosine (C).</p>',
    'G': f'<p style="font-family:sans-serif; color:#FF6768; font-size: 20px;">There are {str(X["G"])}' + ' guanine (G).</p>',
    'T': f'<p style="font-family:sans-serif; color:#139487; font-size: 20px;">There are {str(X["T"])}' + ' thymine (T).</p>'
  }
  
  st.markdown(title_colors['A'], unsafe_allow_html=True)
  st.markdown(title_colors['C'], unsafe_allow_html=True)
  st.markdown(title_colors['G'], unsafe_allow_html=True)
  st.markdown(title_colors['T'], unsafe_allow_html=True)

  ### 3. Display Count DataFrame via Pandas (pd)
  st.subheader('Nucleotide Count DataFrame')
  dfc = pd.DataFrame.from_dict(X, orient='index')
  dfc = dfc.rename({0: 'count'}, axis='columns')
  dfc.reset_index(inplace=True)
  dfc = dfc.rename(columns = {'index':'nucleotide'})
  st.write(dfc)

  ### 4. Display Bar Chart using Altair
  st.subheader('Visualizing the Nucleotide Count DataFrame')

  p = alt.Chart(dfc).mark_bar().encode(
      x='nucleotide',
      y = 'count',
      color = alt.Color('nucleotide')
  )

  p = p.properties(
      width=alt.Step(80)  # controls width of bar.
  )
  st.write(p)
  st.write('''
  ***
  ''')

  # DNA nucleotide percentages
  st.header('Frequency of each DNA Nucleotide')

  ### 5. Display Percentage DataFrame via Pandas (pd) and NumPy (np)
  st.subheader('Percentage DataFrame')

  # Array Manipulation with np
  nucleotide_count_list = np.array([X['A'], X['C'], X['G'], X['T']])
  nucleotide_rate = (nucleotide_count_list/total_nucleotides) * 100

  ########################
  # function binds nucleotide:count via a dictionary

  percentDict = dict([
    ('A', nucleotide_rate[0]),
    ('C', nucleotide_rate[1]),
    ('G', nucleotide_rate[2]),
    ('T', nucleotide_rate[3])
    ])

  ###################################

  # Display Percentage DataFrame 
  dfp = pd.DataFrame.from_dict(percentDict, orient='index')
  dfp = dfp.rename({0: '%'}, axis='columns')
  dfp.reset_index(inplace=True)
  dfp = dfp.rename(columns = {'index':'nucleotide'})
  st.write(dfp)

  ### 6. Display Percentage Chart using Altair
  st.subheader('6. Display Percentage Chart')

  p2 = alt.Chart(dfp).mark_bar().encode(
      x = 'nucleotide',
      y = alt.Y('%', scale=alt.Scale(domain=(18,28))),
      color = alt.Color('nucleotide')
  )

  p2 = p2.properties(
      width=alt.Step(80)  # controls width of bar.
  )
  st.write(p2)