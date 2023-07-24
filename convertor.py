import json
import yaml
import xmltodict
import os

def xml_to_json(xml_string):
    json_data = xmltodict.parse(xml_string)
    return json.dumps(json_data, indent=4)

def json_to_yaml(json_string):
    json_data = json.loads(json_string)
    return yaml.dump(json_data, indent=4, sort_keys=False)

def json_to_xml(json_string):
    json_data = json.loads(json_string)
    return xmltodict.unparse(json_data, pretty=True)

def yaml_to_json(yaml_string):
    yaml_data = yaml.safe_load(yaml_string)
    return json.dumps(yaml_data, indent=4)

def get_file_extension(file_path):
    _, ext = os.path.splitext(file_path)
    return ext.lower()


if __name__ == "__main__":
    import os

    input_file = input("Enter the path to the file: ")

    if not os.path.isfile(input_file):
        print("Error: File not found.")
    else:
        with open(input_file, "r") as file:
            data = file.read()

        input_format = get_file_extension(input_file)

        valid_output_formats = ["json", "yaml", "yml", "xml"]
        output_format = input("Enter the desired output format (json/yaml-yml/xml): ").lower()

        if output_format not in valid_output_formats:
            print("Invalid output format. Please choose between json, yaml, or xml.")
        else:
            output_file = os.path.splitext(input_file)[0] + "." + output_format

            if input_format == ".xml":  
                if output_format == "yaml":
                    json_data = xml_to_json(data)
                    output = json_to_yaml(json_data)
                elif output_format == "json":
                    output = xml_to_json(data)
            elif input_format == ".json":  
                if output_format == "yaml":
                    output = json_to_yaml(data)
                elif output_format == "xml":
                    output = json_to_xml(data)
            elif input_format == ".yaml" or input_format == ".yml":  
                if output_format == "json":
                    output = yaml_to_json(data)
                elif output_format == "xml":
                    json_data = yaml_to_json(data)
                    output = json_to_xml(json_data)
            else:
                print("Unsupported file format.")

            with open(output_file, "w") as outfile:
                outfile.write(output)

            print(f"'{input_file}' file converted and saved to '{output_file}' successfully.")
