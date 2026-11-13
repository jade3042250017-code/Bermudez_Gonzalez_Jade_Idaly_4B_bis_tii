import pytest
from app_movil import (
    PerfilMovil,
    PerfilPro,
    SuscripcionExpiradaError,
    PuntosInsuficientesError,
)


@pytest.fixture
def perfil_basico():
    return PerfilMovil(username="jade_dev")


def test_creacion_perfil_movil_valores_por_defecto(perfil_basico):
    assert perfil_basico.username == "jade_dev"
    assert perfil_basico.gemas == 50
    assert perfil_basico.racha_dias == 1
    assert perfil_basico.notificaciones_activas is True


def test_gastar_gemas_valido(perfil_basico):
    saldo_final = perfil_basico.gastar_gemas(20)
    assert saldo_final == 30
    assert perfil_basico.gemas == 30


def test_gemas_iniciales_negativas_lanza_error():
    with pytest.raises(ValueError):
        PerfilMovil(username="usuario_invalido", gemas=-10)


@pytest.mark.parametrize("cantidad_invalida", [0, -5, -100])
def test_ganar_gemas_invalido_lanza_error(perfil_basico, cantidad_invalida):
    with pytest.raises(ValueError):
        perfil_basico.ganar_gemas(cantidad_invalida)


def test_gastar_gemas_insuficientes_lanza_error(perfil_basico):
    with pytest.raises(PuntosInsuficientesError):
        perfil_basico.gastar_gemas(100)


def test_gastar_gemas_negativas_o_cero_lanza_error(perfil_basico):
    with pytest.raises(ValueError):
        perfil_basico.gastar_gemas(0)
    with pytest.raises(ValueError):
        perfil_basico.gastar_gemas(-15)


@pytest.mark.parametrize(
    "gemas_ganadas, saldo_esperado",
    [
        (1, 51),
        (10, 60),
        (50, 100),
        (250, 300),
    ],
)
def test_ganar_gemas_parametrizado(perfil_basico, gemas_ganadas, saldo_esperado):
    resultado = perfil_basico.ganar_gemas(gemas_ganadas)
    assert resultado == saldo_esperado
    assert perfil_basico.gemas == saldo_esperado


def test_perfil_pro_herencia_y_descarga_exitosa():
    pro = PerfilPro(username="jade_pro", meses_suscripcion=3)
    assert isinstance(pro, PerfilPro)
    assert isinstance(pro, PerfilMovil)
    assert pro.es_pro is True
    assert pro.meses_suscripcion == 3

    mensaje = pro.descargar_contenido_offline()
    assert "jade_pro" in mensaje


def test_perfil_pro_meses_iniciales_invalidos():
    with pytest.raises(ValueError):
        PerfilPro(username="jade_pro", meses_suscripcion=0)


def test_perfil_pro_suscripcion_expirada():
    pro = PerfilPro(username="jade_pro", meses_suscripcion=1)
    # Simulamos que el tiempo de suscripción llega a 0
    pro.meses_suscripcion = 0

    with pytest.raises(SuscripcionExpiradaError):
        pro.descargar_contenido_offline()

    assert pro.es_pro is False