from odoo import models, fields

class Kelas(models.Model):
    _name = 'addons_sekolah.kelas'
    _description = 'Data Kelas'

    name = fields.Char(string='Nama Kelas', required=True)
    siswa_ids = fields.One2many('addons_sekolah.siswa', 'kelas_id', string='Siswa')
    wali_kelas_id = fields.Many2one('addons_sekolah.guru', string='Wali Kelas')