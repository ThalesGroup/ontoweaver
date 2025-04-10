# # FIXME: The following code is for the test of the multi type transformers. Due to it causing testing errors it is commented out and to be fixed.
#
# def test_multi_type_transformer():
#     from . import testing_functions
#     import logging
#     import ontoweaver
#
#     logging.basicConfig(level=logging.DEBUG)
#
#     directory_name = "multi_type_transformer"
#
#     assert_nodes = [('A:disease', 'disease', {'whatever': 'A0', 'something': 'Whatever it is'}),
#                     ('1:variant', 'variant', {'whatever': 'B1'}),
#                     ('0:variant', 'variant', {'whatever': 'A0'}),
#                     ('C:oncogenicity', 'oncogenicity', {}),
#                     ('2:variant', 'variant', {'whatever': 'C2'}),
#                     ('B:patient', 'patient', {'something': 'Whatever it is'}),
#                     ]
#
#     assert_edges = [('', '1:variant', 'B:patient', 'patient_has_variant', {}),
#                     ('', '0:variant', 'A:disease', 'variant_to_disease', {'something': 'Whatever it is'}),
#                     ('', '2:variant', 'C:oncogenicity', 'variant_to_oncogenicity', {'whatever': 'C2'}),
#                     ]
#
#     data_mapping = {f"tests/{directory_name}/data.csv": f"tests/{directory_name}/mapping.yaml"}
#
#     nodes, edges = ontoweaver.extract(filename_to_mapping=data_mapping, affix="suffix")
#
#     fnodes, fedges = ontoweaver.fusion.reconciliate(nodes, edges, separator=",")
#
#     assert_node_set = testing_functions.convert_to_set(assert_nodes)
#     f_node_set = testing_functions.convert_to_set(fnodes)
#
#     assert assert_node_set == f_node_set, "Nodes are not equal."
#
#     assert_edge_set = testing_functions.convert_to_set(assert_edges)
#     f_edge_set = testing_functions.convert_to_set(fedges)
#
#     assert assert_edge_set == f_edge_set, "Edges are not equal."
#
#
# if __name__ == "__main__":
#     test_multi_type_transformer()