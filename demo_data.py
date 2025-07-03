tomato_classes = [
    'Bacterial Spot', 'Early Blight', 'Late Blight', 'Leaf Mold',
    'Septoria Leaf Spot', 'Spider Mites', 'Target Spot',
    'Yellow Leaf Curl Virus', 'Mosaic Virus', 'Healthy'
]

treatments = {
    'Bacterial Spot': {
        'description': 'Bacterial disease causing small, water-soaked spots.',
        'organic': {
            'treatment': 'Remove infected leaves, apply copper sprays.',
            'instructions': 'Apply copper soap weekly.',
            'products': [{'name': 'Garden Safe Copper Soap', 'price': '$10.99', 'type': 'Organic'}]
        },
        'chemical': {
            'treatment': 'Use bactericides like streptomycin.',
            'instructions': 'Apply every 7–10 days.',
            'products': [{'name': 'Bonide Copper Fungicide', 'price': '$16.99', 'type': 'Chemical'}]
        }
    },
    'Early Blight': {
        'description': 'Fungal disease with dark brown spots and concentric rings.',
        'organic': {
            'treatment': 'Apply neem oil, remove debris.',
            'instructions': 'Spray neem oil every 7–14 days.',
            'products': [{'name': 'Bonide Neem Oil', 'price': '$11.98', 'type': 'Organic'}]
        },
        'chemical': {
            'treatment': 'Apply chlorothalonil or copper-based fungicides.',
            'instructions': 'Spray every 7–10 days.',
            'products': [{'name': 'Spectracide Immunox', 'price': '$12.97', 'type': 'Chemical'}]
        }
    },
    'Late Blight': {
        'description': 'Rapidly spreading fungal disease that causes dark lesions.',
        'organic': {
            'treatment': 'Remove infected plants, use compost tea or copper.',
            'instructions': 'Spray compost tea every 5–7 days.',
            'products': [{'name': 'Dr. Earth Fungicide', 'price': '$13.99', 'type': 'Organic'}]
        },
        'chemical': {
            'treatment': 'Apply chlorothalonil or mancozeb.',
            'instructions': 'Spray at first sign, repeat every 7 days.',
            'products': [{'name': 'Daconil Fungicide', 'price': '$14.49', 'type': 'Chemical'}]
        }
    },
    'Leaf Mold': {
        'description': 'Fungal disease causing yellow patches on leaves.',
        'organic': {
            'treatment': 'Improve air circulation, apply baking soda spray.',
            'instructions': 'Spray weekly during humid conditions.',
            'products': [{'name': 'Safer Brand Garden Fungicide', 'price': '$9.89', 'type': 'Organic'}]
        },
        'chemical': {
            'treatment': 'Use fungicides containing chlorothalonil.',
            'instructions': 'Spray every 7–10 days as needed.',
            'products': [{'name': 'Ortho MAX Garden Disease Control', 'price': '$12.79', 'type': 'Chemical'}]
        }
    },
    'Septoria Leaf Spot': {
        'description': 'Fungal disease causing small, circular spots with dark borders.',
        'organic': {
            'treatment': 'Remove infected leaves, apply neem oil.',
            'instructions': 'Spray neem oil weekly.',
            'products': [{'name': 'Monterey Neem Oil', 'price': '$15.25', 'type': 'Organic'}]
        },
        'chemical': {
            'treatment': 'Use fungicides like mancozeb or chlorothalonil.',
            'instructions': 'Apply every 7–10 days.',
            'products': [{'name': 'Bonide Fung-onil', 'price': '$14.99', 'type': 'Chemical'}]
        }
    },
    'Spider Mites': {
        'description': 'Tiny pests that cause speckled, discolored leaves.',
        'organic': {
            'treatment': 'Spray insecticidal soap or neem oil.',
            'instructions': 'Spray early morning every 3–5 days.',
            'products': [{'name': 'Safer Brand Insecticidal Soap', 'price': '$8.99', 'type': 'Organic'}]
        },
        'chemical': {
            'treatment': 'Use miticides or acaricides.',
            'instructions': 'Apply per label directions every 7 days.',
            'products': [{'name': 'Ortho Insect Mite & Disease Control', 'price': '$16.49', 'type': 'Chemical'}]
        }
    },
    'Target Spot': {
        'description': 'Fungal disease causing brown, ring-like spots on leaves.',
        'organic': {
            'treatment': 'Apply copper fungicide or neem oil.',
            'instructions': 'Spray weekly or after rain.',
            'products': [{'name': 'Southern Ag Copper Fungicide', 'price': '$10.55', 'type': 'Organic'}]
        },
        'chemical': {
            'treatment': 'Use chlorothalonil or strobilurin fungicides.',
            'instructions': 'Spray every 7 days.',
            'products': [{'name': 'Daconil Fungicide', 'price': '$14.49', 'type': 'Chemical'}]
        }
    },
    'Yellow Leaf Curl Virus': {
        'description': 'Viral disease transmitted by whiteflies, causes leaf curling and yellowing.',
        'organic': {
            'treatment': 'Remove infected plants, control whiteflies with neem oil.',
            'instructions': 'Spray neem oil every 7 days.',
            'products': [{'name': 'Bonide Neem Oil', 'price': '$11.98', 'type': 'Organic'}]
        },
        'chemical': {
            'treatment': 'Use insecticides to control whiteflies.',
            'instructions': 'Apply systemic insecticides biweekly.',
            'products': [{'name': 'Bayer Advanced Insect Killer', 'price': '$13.75', 'type': 'Chemical'}]
        }
    },
    'Mosaic Virus': {
        'description': 'Viral disease causing mottled patterns on leaves.',
        'organic': {
            'treatment': 'Remove and destroy infected plants, sanitize tools.',
            'instructions': 'Maintain hygiene and plant resistance strategies.',
            'products': [{'name': 'Garden Safe Fungicide3', 'price': '$9.49', 'type': 'Organic'}]
        },
        'chemical': {
            'treatment': 'No chemical cure; control aphids and pests.',
            'instructions': 'Use insecticides to manage pest vectors.',
            'products': [{'name': 'Sevin Insect Killer', 'price': '$10.99', 'type': 'Chemical'}]
        }
    },
    'Healthy': {
        'description': 'The plant appears healthy.',
        'organic': {
            'treatment': 'Use compost tea monthly.',
            'instructions': 'Maintain hygiene & monitor plant.',
            'products': [{'name': 'Dr. Earth Compost Tea', 'price': '$12.99', 'type': 'Organic'}]
        },
        'chemical': {
            'treatment': 'Preventive fungicides if needed.',
            'instructions': 'Spray every 14 days if required.',
            'products': [{'name': 'Spectracide Immunox', 'price': '$12.97', 'type': 'Chemical'}]
        }
    }
}
