# -*- coding: utf-8 -*-
"""
This Python module implements a barcode-detection algorithm that
identifies barcodes in natural images. For 'Interleaved 2 of 5' barcodes, a 
barcode parser is implemented that translates a detected barcode in a 1D (bit)
string.

The implementation of the barcode detection (function extractBarcode) is 
loosely based on 'The Ultimate Guide to Barcode Detection' by Adrian Rosebrock.

Created on Sun Mar 18 11:37:02 2018

@author: Jan Verwaeren
"""

from skimage import io, color, filters, morphology, measure
import numpy as np
import matplotlib.pyplot as plt

##############################################################################
# function defenitions
##############################################################################

def extractBarcodeBBox(im_array, show = False):
    
    """
    Funtion that detects a barcode in an image.
    
    PARAMETERS
    ---------
    
    im_array : np.array or str
        If np_array is a numpy array, it should be an (n x m x 3)  RGB matrix; if 
        im_array is a string, it is assumed to be an image filename (png or jpg).
    
    show : bool
        if show is True, the image is shown with an indication of the 'detected' ROI of the barcode.
        
    RETURNS
    -------
    
    A dictionary containing the coordinates of the bounding box of the barcode in the image, as well as 
    a number of additional features (see implementation for details)
    
    """
    
    if type(im_array) is str:
        im_array = io.imread(im_array)
    
    # convert to greyscale en compute h and v derivative
    im = color.rgb2gray(im_array)
    edge_h = filters.scharr_h(im)
    edge_v = filters.scharr_v(im)
    # apply mean filter to absolute difference of vertival and horizontal edginess
    diff = np.abs(edge_v) - np.abs(edge_h)
    diff[diff<0] = 0
    diff[diff>1] = 1
    
    #tmp = filters.rank.mean(diff, footprint = np.ones((25,25)))
    bar = filters.rank.mean(diff, footprint = np.ones((30,30))) > 5
    
    # apply morphological operations to clean up binary image
    strel = morphology.rectangle(10, 30)
    closed = morphology.closing(bar, strel)
    
    processed = closed.copy()
    for i in range(4):
        processed =  morphology.erosion(processed, footprint = np.ones((5,5)))
    for i in range(4):
        processed =  morphology.dilation(processed, footprint = np.ones((5,5)))
    
    processed = morphology.remove_small_objects(processed, 1000)
    
    # compute region properties (mainly bounding box of barcode)
    labeled = morphology.label(processed)
    props = measure.regionprops(labeled)
    bar_prop = sorted(props, key = lambda x : x.area  , reverse=True)[0]
    
    # computed paramters bbox
    padding = 3
    bbox = (bar_prop.bbox[0]-padding, bar_prop.bbox[1]-padding, bar_prop.bbox[2]+padding, bar_prop.bbox[3]+padding)
    #bbox = bar_prop.bbox
    xy = (bbox[1], bbox[0]) # coord minx miny
    width, height = bbox[3] - bbox[1], bbox[2] - bbox[0]
    row = bbox[0]
    col = bbox[1]
    
    barcode = {'bbox' : bbox, 'xy' : xy, 'width' : width, 'height' : height, 'row' : row, 'col' : col}
    bar_img = im[barcode['row'] : barcode['row'] + barcode['height'], barcode['col'] : barcode['col'] + barcode['width']]
    
    central_line = bar_img[int(barcode['height']/2),:]
    barcode['central_line'] = central_line
    
    # show result
    if show:
        f = plt.figure(1)
        plt.imshow(im_array)
        rect = plt.Rectangle((bbox[1], bbox[0]), bbox[3] - bbox[1], bbox[2] - bbox[0], fill = False, edgecolor = (0,1,0), lw = 2)
        f.axes[0].add_patch(rect)
        f.canvas.draw_idle()
    
    return barcode


def centralLineToBitstring(centralLine_array, plot = False):
    """
    Function to transform the central line (an array) of a barcode into a bitstring.
    
    """
    m = np.mean(centralLine_array[10:-10])
    
    if plot:
        plt.plot(centralLine_array)
        plt.plot([0,len(centralLine_array)], [m,m], '--')
    
    centralLine_bool = centralLine_array < m
    
    changepoints = [i for i in range(1,len(centralLine_bool)) if centralLine_bool[i-1] != centralLine_bool[i]]
    lengths = [changepoints[i] - changepoints[i-1] for i in range(1,len(changepoints))]
    slThreshold = max(lengths)*3/5
    bitstring_lst = []
    for i in range(len(lengths)):
        if i % 2 == 0:
            if lengths[i] > slThreshold:
                bitstring_lst.append('11')
            else:
                bitstring_lst.append('1')
        else:
            if lengths[i] > slThreshold:
                bitstring_lst.append('00')
            else:
                bitstring_lst.append('0')

    bitstring_str = "".join(bitstring_lst)
    
    return bitstring_str
    

def extraheerBarcode(img_fileName):
    """
        Function to detect a barcode in an image, and return the barcode as 
        a bitstring.
        
        PARAMETERS
        ----------
        img_fileName : str
            Filename of an image file (vb: 'testfoto.png')
        
        RETURNS
        -------
        bitstring : str
            bitstring of the detected barcode
        
    """
    img = io.imread(img_fileName)
    barcode = extractBarcodeBBox(img, show=True)
    bitstring = centralLineToBitstring(barcode['central_line'], plot=True)
    return bitstring






