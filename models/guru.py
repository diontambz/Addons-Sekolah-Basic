from odoo import models, fields, api

class Guru(models.Model):
    _name = 'addons_sekolah.guru'
    _description = 'Data Guru'

    nip = fields.Char(string='NIP', required=True)
    name = fields.Char(string='Nama Guru', required=True)
    jns_kelamin = fields.Selection([('laki-laki', 'Laki-laki'), ('perempuan', 'Perempuan')], string='Jenis Kelamin')
    mata_pelajaran_id = fields.Many2one('addons_sekolah.mata_pelajaran', string='Mata Pelajaran')
    usia = fields.Integer(string='Usia')
    no_telp = fields.Char(string='No. Telepon')
    alamat = fields.Text(string='Alamat')