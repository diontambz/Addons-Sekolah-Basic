from odoo import models, fields

class MataPelajaran(models.Model):
    _name = 'addons_sekolah.mata_pelajaran'
    _description = 'Mata Pelajaran'

    name = fields.Char(string='Nama Mata Pelajaran', required=True)
    jurusan = fields.Char(string='Jurusan')