from django.shortcuts import render, redirect
from django.http import JsonResponse
import pickle
import joblib
import PIL
import os
import pickle
from mpl_toolkits.axes_grid1 import ImageGrid
import math

def shop_site():
    render('index.html')
