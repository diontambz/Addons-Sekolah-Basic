from odoo import models, fields

class Jadwal(models.Model):
    _name = 'addons_sekolah.jadwal'
    _description = 'Jadwal Pelajaran'

    hari = fields.Selection([
        ('senin', 'Senin'),
        ('selasa', 'Selasa'),
        ('rabu', 'Rabu'),
        ('kamis', 'Kamis'),
        ('jumat', 'Jumat'),
        ('sabtu', 'Sabtu'),
    ], string='Hari', required=True)
    kelas_id = fields.Many2one('addons_sekolah.kelas', string='Kelas', required=True)
    jam = fields.Float(string='Jam')
    mata_pelajaran_id = fields.Many2one('addons_sekolah.mata_pelajaran', string='Mata Pelajaran', required=True)