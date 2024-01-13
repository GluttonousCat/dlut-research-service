# ! /urs/bin/python3.10
# ! -*- coding:utf-8 -*-


class WosData:
    # 记录每篇论文信息
    def __init__(self):
        self.TI_name = ''
        self.AF = []
        self.DE = []
        self.SO = ''
        self.CR = []
        self.WC = []
        self.PY = ''
        self.ESI = ''
        self.Nation = []
        self.Organization = []
        self.NR = ''
        self.TC = ''
        self.AB = ''
        self.r_background = ''
        self.r_method = ''
        self.r_result = ''
        self.r_conclusion = ''


class AuthorInformation:
    def __init__(self):
        self.AuthorOrganization = []
        self.AuthorNation = ''
        self.AuthorName = ''


WOS_categoryList = (
    'Acoustics',
    'Agricultural Economics & Policy',
    'Agricultural Engineering',
    'Agriculture, Dairy & Animal Science',
    'Agriculture, Multidisciplinary',
    'Agronomy',
    'Allergy',
    'Anatomy & Morphology',
    'Andrology',
    'Anesthesiology',
    'Anthropology',
    'Archaeology',
    'Architecture',
    'Area Studies',
    'Art',
    'Asian Studies',
    'Astronomy & Astrophysics',
    'Audiology & Speech-Language Pathology',
    'Automation & Control Systems',
    'Behavioral Sciences',
    'Biochemical Research Methods',
    'Biochemistry & Molecular Biology',
    'Biodiversity Conservation',
    'Biology',
    'Biophysics',
    'Biotechnology & Applied Microbiology',
    'Business',
    'Business, Finance',
    'Cardiac & Cardiovascular Systems',
    'Cell & Tissue Engineering',
    'Cell Biology',
    'Chemistry, Analytical',
    'Chemistry, Applied',
    'Chemistry, Inorganic & Nuclear',
    'Chemistry, Medicinal',
    'Chemistry, Multidisciplinary',
    'Chemistry, Organic',
    'Chemistry, Physical',
    'Classics',
    'Clinical Neurology',
    'Communication',
    'Computer Science, Artificial Intelligence',
    'Computer Science, Cybernetics',
    'Computer Science, Hardware & Architecture',
    'Computer Science, Information Systems',
    'Computer Science, Interdisciplinary Applications',
    'Computer Science, Software Engineering',
    'Computer Science, Theory & Methods',
    'Construction & Building Technology',
    'Criminology & Penology',
    'Critical Care Medicine',
    'Crystallography',
    'Cultural Studies',
    'Dance',
    'Demography',
    'Dentistry, Oral Surgery & Medicine',
    'Dermatology',
    'Developmental Biology',
    'Ecology',
    'Economics',
    'Education & Educational Research',
    'Education, Scientific Disciplines',
    'Education, Special',
    'Electrochemistry',
    'Emergency Medicine',
    'Endocrinology & Metabolism',
    'Energy & Fuels',
    'Engineering, Aerospace',
    'Engineering, Biomedical',
    'Engineering, Chemical',
    'Engineering, Civil',
    'Engineering, Electrical & Electronic',
    'Engineering, Environmental',
    'Engineering, Geological',
    'Engineering, Industrial',
    'Engineering, Manufacturing',
    'Engineering, Marine',
    'Engineering, Mechanical',
    'Engineering, Multidisciplinary',
    'Engineering, Ocean',
    'Engineering, Petroleum',
    'Entomology',
    'Environmental Sciences',
    'Environmental Studies',
    'Ergonomics',
    'Ethics',
    'Ethnic Studies',
    'Evolutionary Biology',
    'Family Studies',
    'Film, Radio, Television',
    'Fisheries',
    'Folklore',
    'Food Science & Technology',
    'Forestry',
    'Gastroenterology & Hepatology',
    'Genetics & Heredity',
    'Geochemistry & Geophysics',
    'Geography',
    'Geography, Physical',
    'Geology',
    'Geosciences, Multidisciplinary',
    'Geriatrics & Gerontology',
    'Gerontology',
    'Health Care Sciences & Services',
    'Health Policy & Services',
    'Hematology',
    'History',
    'History & Philosophy of Science',
    'History of Social Sciences',
    'Horticulture',
    'Hospitality, Leisure, Sport & Tourism',
    'Humanities, Multidisciplinary',
    'Imaging Science & Photographic Technology',
    'Immunology',
    'Industrial Relations & Labor',
    'Infectious Diseases',
    'Information Science & Library Science',
    'Instruments & Instrumentation',
    'Integrative & Complementary Medicine',
    'International Relations',
    'Language & Linguistics',
    'Law',
    'Limnology',
    'Linguistics',
    'Literary Reviews',
    'Literary Theory & Criticism',
    'Literature',
    'Literature, African, Australian, Canadian',
    'Literature, American',
    'Literature, British Isles',
    'Literature, German, Dutch, Scandinavian',
    'Literature, Romance',
    'Literature, Slavic',
    'Logic',
    'Management',
    'Marine & Freshwater Biology',
    'Materials Science, Biomaterials',
    'Materials Science, Ceramics',
    'Materials Science, Characterization & Testing',
    'Materials Science, Coatings & Films',
    'Materials Science, Composites',
    'Materials Science, Multidisciplinary',
    'Materials Science, Paper & Wood',
    'Materials Science, Textiles',
    'Mathematical & Computational Biology',
    'Mathematics',
    'Mathematics, Applied',
    'Mathematics, Interdisciplinary Applications',
    'Mechanics',
    'Medical Ethics',
    'Medical Informatics',
    'Medical Laboratory Technology',
    'Medicine, General & Internal',
    'Medicine, Legal',
    'Medicine, Research & Experimental',
    'Medieval & Renaissance Studies',
    'Metallurgy & Metallurgical Engineering',
    'Meteorology & Atmospheric Sciences',
    'Microbiology',
    'Microscopy',
    'Mineralogy',
    'Mining & Mineral Processing',
    'Multidisciplinary Sciences',
    'Music',
    'Mycology',
    'Nanoscience & Nanotechnology',
    'Neuroimaging',
    'Neurosciences',
    'Nuclear Science & Technology',
    'Nursing',
    'Nutrition & Dietetics',
    'Obstetrics & Gynecology',
    'Oceanography',
    'Oncology',
    'Operations Research & Management Science',
    'Ophthalmology',
    'Optics',
    'Ornithology',
    'Orthopedics',
    'Otorhinolaryngology',
    'Paleontology',
    'Parasitology',
    'Pathology',
    'Pediatrics Vascular Disease',
    'Pharmacology & Pharmacy',
    'Philosophy',
    'Physics, Applied',
    'Physics, Atomic, Molecular & Chemical',
    'Physics, Condensed Matter',
    'Physics, Fluids & Plasmas',
    'Physics, Mathematical',
    'Physics, Multidisciplinary',
    'Physics, Nuclear',
    'Physics, Particles & Fields',
    'Physiology',
    'Planning & Development',
    'Plant Sciences',
    'Poetry',
    'Political Science',
    'Polymer Science',
    'Primary Health Care',
    'Psychiatry',
    'Psychology',
    'Psychology, Applied',
    'Psychology, Biological',
    'Psychology, Clinical',
    'Psychology, Developmental',
    'Psychology, Educational',
    'Psychology, Experimental',
    'Psychology, Mathematical',
    'Psychology, Multidisciplinary',
    'Psychology, Psychoanalysis',
    'Psychology, Social',
    'Public Administration',
    'Public, Environmental & Occupational Health',
    'Radiology, Nuclear Medicine & Medical Imaging',
    'Rehabilitation',
    'Religion',
    'Remote Sensing',
    'Reproductive Biology',
    'Respiratory System',
    'Rheumatology',
    'Robotics',
    'Social Issues',
    'Social Sciences, Biomedical',
    'Social Sciences, Interdisciplinary',
    'Social Sciences, Mathematical Methods',
    'Social Work',
    'Sociology',
    'Soil Science',
    'Spectroscopy',
    'Sport Sciences',
    'Statistics & Probability',
    'Substance Abuse',
    'Surgery',
    'Telecommunications',
    'Theater',
    'Thermodynamics',
    'Toxicology',
    'Transplantation',
    'Transportation',
    'Transportation Science & Technology',
    'Tropical Medicine',
    'Urban Studies',
    'Urology & Nephrology',
    'Veterinary Sciences',
    'Virology',
    'Water Resources',
    'Women\'s Studies',
    'Zoology',
)
NationList = (
    'USA',
    'Abkhazia',
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Commonwealth oftheBahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'BurundiCambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Catalen',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombia',
    'Comoros',
    'Congo (Brazzaville)',
    'Congo (Kinshasa)',
    'Cook Islands',
    'Costa Rica',
    'Côte d\'Ivoire',
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech RepublicDenmark',
    'Djibouti',
    'Donetsk People\'s Republic',
    'Dominica',
    'Dominican Republic',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'England',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'South Korea',
    'Kosovo',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Maltese Knights',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Montenegro',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Nagorno-Karabakh',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Niue',
    'Northern Cyprus',
    'North Macedonia',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Palestine',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'People\'s Republic of Korea',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Pridnestrovie',
    'Puntland',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Christopher and Nevis',
    'Saint Lucia',
    'Saint Vincent and the Grenadines',
    'Samoa',
    'San Marino',
    'São Tomé and Príncipe',
    'Saudi Arabia',
    'Senegal',
    'Serbia',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somali',
    'Somaliland',
    'South Africa',
    'South Ossetia',
    'South Sudan',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Timor-Leste',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican city(the Holy see)',
    'Venezuela',
    'Vietnam',
    'Western Sahara',
    'Yemen',
    'Zambia',
    'Zimbabwe'
)
