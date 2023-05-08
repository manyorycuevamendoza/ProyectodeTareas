from app import app,db
from flask import render_template
from flask import Flask
import json
from flask_cors import cross_origin,CORS
from flask import request
import datetime
from app.models import Usuario,Tarea,Tipo_tarea
from conexion_WhatsApp import notificacion
from conexion_Gmail import correo