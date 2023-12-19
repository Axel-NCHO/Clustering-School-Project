import ast

# ##########
# Concepts and control function detection using AST
# ##########

# Implemented concepts keys
NB_VAR_AFFECTATION_CONCEPT = "nb-var-affectation-concept"
NB_BOOLEAN_CONCEPT = "nb-boolean-concept"
NB_STRING_CONCEPT = "nb-string-concept"
NB_IF_BRANCH_CONCEPT = "nb-if-branch-concept"
NB_ELIF_BRANCH_CONCEPT = "nb-elif-branch-concept"
NB_ELSE_BRANCH_CONCEPT = "nb-else-branch-concept"
NB_FOR_SIMPLE_CONCEPT = "nb-for-simple-concept"
NB_FOR_COUNTER_0_CONCEPT = "nb-for-counter-0-concept"
NB_FOR_COUNTER_N_CONCEPT = "nb-for-counter-n-concept"
NB_WHILE_CONCEPT = "nb-while-concept"

# Used control functions keys
NB_WALK_CTR_FCT = "walk"
NB_LEFT_CTR_FCT = "left"
NB_RIGHT_CTR_FCT = "right"
NB_OPEN_CTR_FCT = "open"
NB_JUMP_CTR_FCT = "jump"
NB_JUMP_HEIGHT_CTR_FCT = "jump-height"
NB_JUMP_HIGH_CTR_FCT = "jump-high"
NB_GET_HEIGHT_CTR_FCT = "get-height"
NB_READ_STRING_CTR_FCT = "read-string"
NB_READ_INT_CTR_FCT = "read-int"
NB_ATTACK_CTR_FCT = "attack"
NB_DETECT_OBSTACLE_CTR_FCT = "detect-obstacle"
NB_TURN_CTR_FCT = "turn"
NB_SHOOT_CTR_FCT = "shoot"

CONCEPT_KEYS = [
    NB_VAR_AFFECTATION_CONCEPT,
    NB_BOOLEAN_CONCEPT,
    NB_STRING_CONCEPT,
    NB_IF_BRANCH_CONCEPT,
    NB_ELIF_BRANCH_CONCEPT,
    NB_ELSE_BRANCH_CONCEPT,
    NB_FOR_SIMPLE_CONCEPT,
    NB_FOR_COUNTER_0_CONCEPT,
    NB_FOR_COUNTER_N_CONCEPT,
    NB_WHILE_CONCEPT
]

CTR_FCT_KEYS = [
    NB_WALK_CTR_FCT,
    NB_LEFT_CTR_FCT,
    NB_RIGHT_CTR_FCT,
    NB_OPEN_CTR_FCT,
    NB_JUMP_CTR_FCT,
    NB_JUMP_HEIGHT_CTR_FCT,
    NB_JUMP_HIGH_CTR_FCT,
    NB_GET_HEIGHT_CTR_FCT,
    NB_READ_STRING_CTR_FCT,
    NB_READ_INT_CTR_FCT,
    NB_ATTACK_CTR_FCT,
    NB_DETECT_OBSTACLE_CTR_FCT,
    NB_TURN_CTR_FCT,
    NB_SHOOT_CTR_FCT
]

ALL_KEYS = CONCEPT_KEYS + CTR_FCT_KEYS

ALLOWED_KEYS_BY_LEVEL = {
    1: CONCEPT_KEYS + [
        NB_WALK_CTR_FCT,
        NB_LEFT_CTR_FCT,
        NB_RIGHT_CTR_FCT,
        NB_OPEN_CTR_FCT
    ],
    2: CONCEPT_KEYS + [
        NB_WALK_CTR_FCT,
        NB_LEFT_CTR_FCT,
        NB_RIGHT_CTR_FCT,
        NB_JUMP_CTR_FCT,
        NB_ATTACK_CTR_FCT,
        NB_OPEN_CTR_FCT
    ],
    3: CONCEPT_KEYS + [
        NB_WALK_CTR_FCT,
        NB_JUMP_HEIGHT_CTR_FCT,
        NB_READ_INT_CTR_FCT,
        NB_OPEN_CTR_FCT,
    ],
    4: CONCEPT_KEYS + [
        NB_WALK_CTR_FCT,
        NB_LEFT_CTR_FCT,
        NB_RIGHT_CTR_FCT,
        NB_READ_STRING_CTR_FCT,
        NB_OPEN_CTR_FCT,
    ],
    5: CONCEPT_KEYS + [
        NB_WALK_CTR_FCT,
        NB_JUMP_CTR_FCT,
        NB_JUMP_HIGH_CTR_FCT,
        NB_GET_HEIGHT_CTR_FCT,
        NB_OPEN_CTR_FCT,
    ],
    6: CONCEPT_KEYS + [
        NB_WALK_CTR_FCT,
        NB_JUMP_HEIGHT_CTR_FCT,
        NB_OPEN_CTR_FCT,
    ],
    7: CONCEPT_KEYS + [
        NB_TURN_CTR_FCT,
        NB_SHOOT_CTR_FCT,
    ],
    8: CONCEPT_KEYS + [
        NB_WALK_CTR_FCT,
        NB_LEFT_CTR_FCT,
        NB_RIGHT_CTR_FCT,
        NB_ATTACK_CTR_FCT,
        NB_DETECT_OBSTACLE_CTR_FCT,
        NB_OPEN_CTR_FCT,
    ],
}

# Control functions
WALK_NAME_FR = "avancer"
LEFT_NAME_FR = "gauche"
RIGHT_NAME_FR = "droite"
OPEN_NAME_FR = "ouvrir"
JUMP_NAME_FR = "sauter"
JUMP_HEIGHT_NAME_FR = "sauter_hauteur"
JUMP_HIGH_NAME_FR = "sauter_haut"
GET_HEIGHT_NAME_FR = "mesurer_hauteur"
READ_STRING_NAME_FR = "lire_chaine"
READ_INT_NAME_FR = "lire_nombre"
ATTACK_NAME_FR = "coup"
DETECT_OBSTACLE_NAME_FR = "detecter_obstacle"
TURN_NAME_FR = "tourner"
SHOOT_NAME_FR = "tirer"

WALK_NAME_EN = "walk"
LEFT_NAME_EN = "left"
RIGHT_NAME_EN = "right"
OPEN_NAME_EN = "open_chest"
JUMP_NAME_EN = "jump"
JUMP_HEIGHT_NAME_EN = "jump_height"
JUMP_HIGH_NAME_EN = "jump_high"
GET_HEIGHT_NAME_EN = "get_height"
READ_STRING_NAME_EN = "read_string"
READ_INT_NAME_EN = "read_number"
ATTACK_NAME_EN = "attack"
DETECT_OBSTACLE_NAME_EN = "detect_obstacle"
TURN_NAME_EN = "turn"
SHOOT_NAME_EN = "shoot"

CONTROL_FUNCTION_NAME_TO_KEY_MAPPING = {
    WALK_NAME_FR: NB_WALK_CTR_FCT,
    LEFT_NAME_FR: NB_LEFT_CTR_FCT,
    RIGHT_NAME_FR: NB_RIGHT_CTR_FCT,
    OPEN_NAME_FR: NB_OPEN_CTR_FCT,
    JUMP_NAME_FR: NB_JUMP_CTR_FCT,
    JUMP_HEIGHT_NAME_FR: NB_JUMP_HEIGHT_CTR_FCT,
    JUMP_HIGH_NAME_FR: NB_JUMP_HIGH_CTR_FCT,
    GET_HEIGHT_NAME_FR: NB_GET_HEIGHT_CTR_FCT,
    READ_STRING_NAME_FR: NB_READ_STRING_CTR_FCT,
    READ_INT_NAME_FR: NB_READ_INT_CTR_FCT,
    ATTACK_NAME_FR: NB_ATTACK_CTR_FCT,
    DETECT_OBSTACLE_NAME_FR: NB_DETECT_OBSTACLE_CTR_FCT,
    TURN_NAME_FR: NB_TURN_CTR_FCT,
    SHOOT_NAME_FR: NB_SHOOT_CTR_FCT,
    WALK_NAME_EN: NB_WALK_CTR_FCT,
    LEFT_NAME_EN: NB_LEFT_CTR_FCT,
    RIGHT_NAME_EN: NB_RIGHT_CTR_FCT,
    OPEN_NAME_EN: NB_OPEN_CTR_FCT,
    JUMP_NAME_EN: NB_JUMP_CTR_FCT,
    JUMP_HEIGHT_NAME_EN: NB_JUMP_HEIGHT_CTR_FCT,
    JUMP_HIGH_NAME_EN: NB_JUMP_HIGH_CTR_FCT,
    GET_HEIGHT_NAME_EN: NB_GET_HEIGHT_CTR_FCT,
    READ_STRING_NAME_EN: NB_READ_STRING_CTR_FCT,
    READ_INT_NAME_EN: NB_READ_INT_CTR_FCT,
    ATTACK_NAME_EN: NB_ATTACK_CTR_FCT,
    DETECT_OBSTACLE_NAME_EN: NB_DETECT_OBSTACLE_CTR_FCT,
    TURN_NAME_EN: NB_TURN_CTR_FCT,
    SHOOT_NAME_EN: NB_SHOOT_CTR_FCT
}


class programParser(ast.NodeVisitor):
    def __init__(self):
        self.features_dict = dict()
        for key in ALL_KEYS:
            self.features_dict[key] = 0

    # Each visit_* function is automatically called depend on node type during
    # tree traversal
    def visit_While(self, node):
        self.features_dict[NB_WHILE_CONCEPT] += 1
        self.generic_visit(node)

    def visit_For(self, node):
        loop_var_name = node.target.id
        is_simple_for = not self.var_used(node, loop_var_name)
        if is_simple_for:
            self.features_dict[NB_FOR_SIMPLE_CONCEPT] += 1
        else:
            for_iter = node.iter
            if isinstance(for_iter, ast.Call):
                if for_iter.func.id == "range":
                    nb_args = len(for_iter.args)
                    if nb_args == 1:
                        self.features_dict[NB_FOR_COUNTER_0_CONCEPT] += 1
                    elif nb_args >= 2:
                        if isinstance(for_iter.args[0], ast.Constant) and for_iter.args[0].value == 0:
                            self.features_dict[NB_FOR_COUNTER_0_CONCEPT] += 1
                        else:
                            self.features_dict[NB_FOR_COUNTER_N_CONCEPT] += 1

        self.generic_visit(node)

    def visit_Assign(self, node):
        self.features_dict[NB_VAR_AFFECTATION_CONCEPT] += 1
        self.generic_visit(node)

    def visit_AugAssign(self, node):
        self.features_dict[NB_VAR_AFFECTATION_CONCEPT] += 1
        self.generic_visit(node)

    def visit_If(self, node):
        is_parent_if = isinstance(node.parent, ast.If)
        # There's probably a bug here, nested if are detected like elif
        if is_parent_if:
            self.features_dict[NB_ELIF_BRANCH_CONCEPT] += 1
        else:
            self.features_dict[NB_IF_BRANCH_CONCEPT] += 1
        has_else = len(node.orelse) != 0 and not isinstance(node.orelse[0], ast.If)
        if has_else:
            self.features_dict[NB_ELSE_BRANCH_CONCEPT] += 1
        self.generic_visit(node)

    def visit_Constant(self, node):
        if isinstance(node.value, str):
            self.features_dict[NB_STRING_CONCEPT] += 1
        elif isinstance(node.value, bool):
            self.features_dict[NB_BOOLEAN_CONCEPT] += 1

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            function_name = node.func.id
            if function_name in CONTROL_FUNCTION_NAME_TO_KEY_MAPPING.keys():
                self.features_dict[CONTROL_FUNCTION_NAME_TO_KEY_MAPPING[function_name]] += 1
        self.generic_visit(node)

    # Check if a variable (name) is used in a sub-tree (node)
    def var_used(self, node, name):
        result = False
        child_nodes = ast.iter_child_nodes(node)
        for child_node in child_nodes:
            child_result = False
            # There's probably a bug here, rather do:
            # if isinstance(child_node,ast.Name) and isinstance(child_node.ctx,ast.Load) and (child_node.id == name):
            #      child_result = True
            if isinstance(child_node, ast.Name) and isinstance(child_node.ctx, ast.Load):
                child_result = (child_node.id == name)
            else:
                child_result = self.var_used(child_node, name)
            result = result or child_result
        return result


#  Add parents nodes in current nodes (used to detect elif statements)
class Parentage(ast.NodeTransformer):
    # current parent (module)
    parent = None

    def visit(self, node):
        # set parent attribute for this node
        node.parent = self.parent
        # This node becomes the new parent
        self.parent = node
        # Do any work required by super class 
        node = super().visit(node)
        # If we have a valid node (ie. node not being removed)
        if isinstance(node, ast.AST):
            # update the parent, since this may have been transformed 
            # to a different node by super
            self.parent = node.parent
        return node
